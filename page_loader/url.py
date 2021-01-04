# -*- coding: utf-8 -*-

"""Url manipulation module."""

import logging
import os
import re
from typing import Dict, List, Tuple
from urllib.parse import urljoin, urlparse

import aiohttp

from page_loader import exceptions
from page_loader.common import debug_logger

log = logging.getLogger(__name__)


async def get_resource(url: str) -> bytes:
    """Get response from url.

    Args:
        url: string

    Raises:
        LoadingError: exceptions.LoadingError

    Returns:
        bytes: the whole response’s body as bytes.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                bytes_of_data = await response.read()
    except aiohttp.ClientError as err:
        log.exception(
            str(err.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise exceptions.LoadingError(
            'HTTP client error while downloading {0}: {1}'.format(url, err),
        )
    return bytes_of_data


def parse_url(url: str) -> Tuple:
    """Parse url into parts.

    Args:
        url: string

    Returns:
        Tuple: url's netloc, path, splitted into filename and extension
    """
    parsed = urlparse(url.strip('/'))
    path_name_part, path_ext_part = os.path.splitext(parsed.path)
    return (parsed.netloc, path_name_part, path_ext_part)


@debug_logger
def sanitize(url: str, keep_extension=False) -> str:
    """Sanitize url.

    Args:
        url: string
        keep_extension: bool

    Returns:
        str: sanitized url
    """
    regex = re.compile(r'[^0-9A-Za-z]')
    netloc, path, ext = parse_url(url)

    sanitized = regex.sub('-', netloc + path)

    if keep_extension:
        return sanitized + ext

    return sanitized


@debug_logger
def make_resource_url(url: str, resource: str) -> str:
    """Create url for resource.

    Args:
        url: string
        resource: string

    Returns:
        str: full url for resource, so we can download it
    """
    return urljoin(url, resource)


@debug_logger
def map_resource_path_to_output_dir(
    urls: List,
    resource_directory_name: str,
) -> Dict:
    """Map resource paths to the output dir.

    For example, converts '/css/main.css' to
    '/tmp/example-com_files/css-main.css'

    Args:
        urls: List of local resources
        resource_directory_name: string

    Returns:
        Dict: map the source paths for the resources to the output dir.
    """
    return {
        resource: os.path.join(
            resource_directory_name,
            sanitize(resource, keep_extension=True),
        )
        for resource in urls
    }


@debug_logger
def is_local_resource(resource_url: str, page_url: str) -> bool:
    """Check if the resource is local to the page.

    Args:
        resource_url: resource src or href attr value
        page_url: url string

    Returns:
        bool: True if resource is local
    """
    resource = urlparse(resource_url)
    page = urlparse(page_url)
    return not resource.netloc or resource.netloc == page.netloc
