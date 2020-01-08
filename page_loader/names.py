# -*- coding: utf-8 -*-

"""Names generator functions."""

import logging
import os
import re
from urllib.parse import urlparse

from page_loader.common import debug_logger

log = logging.getLogger(__name__)


@debug_logger
def create_resources_dir_name(path):
    """Create local resources dir name."""
    return path.replace('.html', '_files')


@debug_logger
def create_resource_name(res):
    """Create local resource file name."""
    log.debug(f'Creating new name for {res}')
    base, ext = os.path.splitext(res)
    base = re.sub(r'[\W_]', '-', base.replace('/', '', 1))
    return f'{base}{ext}'


@debug_logger
def create_html_file_name(res):
    """Create html page file name."""
    parsed = urlparse(res)
    scheme = parsed.scheme
    page_name = parsed.geturl().replace(scheme, '', 1).replace('://', '')
    if page_name.endswith('.html'):
        page_name = page_name.replace('.html', '')
    page_name = re.sub(r'[\W_]', '-', page_name)
    return f'{page_name}.html'
