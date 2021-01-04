# -*- coding: utf-8 -*-

"""Data parsing module."""

import logging
from typing import List

import bs4

from page_loader.common import LOCAL_RESOURCES, debug_logger
from page_loader.url import get_resource, is_local_resource

log = logging.getLogger(__name__)


async def parse_page(url: str) -> bs4.BeautifulSoup:
    """Convert url's content into BeautifulSoup object.

    Args:
        url: string

    Returns:
        bs4.BeautifulSoup: bs4.BeautifulSoup object
    """
    page = await get_resource(url)
    return bs4.BeautifulSoup(page.decode(), 'html.parser')


def stringify_page(page: bs4.BeautifulSoup) -> str:
    """Convert BeautifulSoup object to string.

    Args:
        page: bs4.BeautifulSoup object

    Returns:
        str: string representation of the BeautifulSoup object
    """
    return page.prettify(formatter='html5')


def find_local_resources(page: bs4.BeautifulSoup, page_url: str) -> List:
    """Get local resources.

    Args:
        page: bs4.BeautifulSoup object
        page_url: string

    Returns:
        List: list of local resources
    """
    res_with_paths = map(
        get_link_from_resource_tag,
        find_resources_in_page(page),
    )
    non_empty_paths = filter(None, res_with_paths)
    return [
        path for path in non_empty_paths if is_local_resource(path, page_url)
    ]


def replace_urls(
    page: bs4.BeautifulSoup,
    local_resources: List,
) -> bs4.BeautifulSoup:
    """Replace urls for local resources.

    Args:
        page: bs4.BeautifulSoup object
        local_resources: List of local resources

    Returns:
        bs4.BeautifulSoup: BeautifulSoup object
    """
    for res in find_resources_in_page(page):
        src = get_link_from_resource_tag(res)
        if src in local_resources:
            attr_name = get_link_attr_name(res)
            res.attrs[attr_name] = local_resources[src]
    return page


def find_resources_in_page(page: bs4.BeautifulSoup) -> List:
    """Get resources from page.

    Args:
        page: BeautifulSoup object

    Returns:
        List: list of tags from LOCAL_RESOURCES
    """
    return page.find_all(LOCAL_RESOURCES.keys())


@debug_logger
def get_link_from_resource_tag(tag: bs4.element.Tag) -> str:
    """Extract link attribute from tag.

    Args:
        tag: bs4.element.Tag

    Returns:
        str: string value of tag's `src` attribute
    """
    return tag.attrs.get(get_link_attr_name(tag))


@debug_logger
def get_link_attr_name(tag: bs4.element.Tag) -> str:
    """Get LOCAL_RESOURCES tags attribute name.

    Args:
        tag: bs4.element.Tag

    Returns:
        str: tag's attribute from LOCAL_RESOURCES dict.
    """
    return LOCAL_RESOURCES.get(tag.name)
