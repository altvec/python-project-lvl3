# -*- coding: utf-8 -*-

"""Common entities of the project."""
import logging
import os
from functools import wraps
from urllib.parse import urlsplit

import requests

log = logging.getLogger(__name__)

LOCAL_RESOURCES = {
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def get_url(url):
    """Get response from url."""
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.HTTPError as err:
        log.exception(
            str(err.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
    return res


def url_site(url):
    """Make site's url."""
    return '://'.join(urlsplit(url)[0:2])


def create_dir(path):
    """Create directory."""
    if not os.path.exists(path):
        os.makedirs(path)


def save(path, data, mode='w'):
    """Save provided data."""
    try:
        with open(path, mode) as f:
            f.write(data)
    except PermissionError:
        log.exception(
            'Permission denied',
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise


def debug_logger(func):
    """Log decorator function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(f'{func.__name__} :: input: {args} {kwargs}')
        result = func(*args, **kwargs)
        log.debug(f'{func.__name__} :: return: {str(result)}')
        return result
    return wrapper
