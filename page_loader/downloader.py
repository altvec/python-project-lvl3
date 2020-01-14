# -*- coding: utf-8 -*-

"""Main module."""

import logging
import os

from bs4 import BeautifulSoup

from page_loader.common import get_url, save, url_site
from page_loader.names import create_html_file_name, create_resources_dir_name
from page_loader.resources import download_resources, find_resources

log = logging.getLogger(__name__)


def download(output, url):
    """Download webpage and it's resources if available."""
    url = url.rstrip('/')
    html_file_path = os.path.join(output, create_html_file_name(url))
    resources_dir_name = create_resources_dir_name(html_file_path)

    soup, resources = find_resources(
        BeautifulSoup(get_url(url).content, 'html.parser'),
        resources_dir_name,
    )

    save(html_file_path, str(soup.prettify()))
    if resources:
        download_resources(
            resources,
            url_site(url),
            resources_dir_name,
        )
