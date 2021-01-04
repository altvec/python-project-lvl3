# -*- coding: utf-8 -*-

"""Data loading module."""

import asyncio
import logging
import os
from pathlib import Path
from typing import List

import tqdm

from page_loader.common import debug_logger
from page_loader.parsing import (
    find_local_resources,
    parse_page,
    replace_urls,
    stringify_page,
)
from page_loader.url import (
    get_resource,
    make_resource_url,
    map_resource_path_to_output_dir,
    sanitize,
)

log = logging.getLogger(__name__)


async def download(url: str, output_dir: Path) -> str:
    """Download function.

    Args:
        url: string with page address
        output_dir: directory to which files will be saved to

    Returns:
        str: location of the saved HMTL page
    """
    page = await parse_page(url)
    page_name = create_html_file_name(url)

    resources_dir_name = create_resources_dir_name(url)
    local_resources = find_local_resources(page, url)
    resource_map = map_resource_path_to_output_dir(
        local_resources,
        resources_dir_name,
    )

    html_file_path = output_dir / page_name
    await save(html_file_path, stringify_page(replace_urls(page, resource_map)))

    if local_resources:
        output_dir_path = output_dir / resources_dir_name
        create_dir(output_dir_path)
        await download_resources(url, resource_map, output_dir_path)

    return html_file_path


async def download_resources(url: str, resources: List, dest: str):
    """Download and save local resources.

    Args:
        url: string
        resources: List of local resources to download to
        dest: destination dir, where resources will be saved
    """
    tasks = []
    for k, v in resources.items():
        resource_url = make_resource_url(url, k)
        resource_path = dest / v.split('/')[-1]
        tasks.append(process_task(resource_url, resource_path))
    # await asyncio.gather(*tasks)
    pbar = tqdm.tqdm(total=len(tasks))
    for f in asyncio.as_completed(tasks):
        value = await f  # noqa: WPS110
        pbar.set_description(value)
        pbar.update()


async def process_task(url: str, path: Path):
    """Download and save resource from url into path.

    Args:
        url: string
        path: directory to which file will be saved to
    """
    bytes_of_data = await get_resource(url)
    await save(path, bytes_of_data, 'wb')


def create_dir(path: Path):
    """Create directory.

    Args:
        path: string
    """
    if not os.path.exists(path):
        os.makedirs(path)


@debug_logger
def create_html_file_name(url: str) -> str:
    """Create html page file name.

    Args:
        url: string

    Returns:
        str: sanitized html file name
    """
    return '{0}.html'.format(sanitize(url))


@debug_logger
def create_resources_dir_name(url: str) -> str:
    """Create local resources dir name.

    Args:
        url: string

    Returns:
        str: sanitized resources dir
    """
    return '{0}_files'.format(sanitize(url))


async def save(path, file_content, mode='w'):
    """Save provided data.

    Args:
        path: string that represents file path
        file_content: file content
        mode: file writing mode

    Raises:
        PermissionError: on write permission errors
    """
    try:
        with open(path, mode) as f:
            f.write(file_content)
    except PermissionError:
        log.exception(
            'Permission denied',
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
