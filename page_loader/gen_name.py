# -*- coding: utf-8 -*-

"""File name generation functions."""

import os
import re

from page_loader.parse_url import parse_url


def generate_name(resource):
    """Generate file name."""
    host, path = parse_url(resource)
    if not host:
        path = path[1:]  # remove leading slash
    base, ext = os.path.splitext(path)
    name = re.sub(r'[\W_]', '-', f'{host}{base}')
    return f'{name}{ext}'
