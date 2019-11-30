# -*- coding: utf-8 -*-

"""Parsing url."""

from urllib.parse import urlparse


def parse_url(url):
    """Parse url and return tuple of params."""
    parsed = urlparse(url)
    return (parsed.netloc, parsed.path)
