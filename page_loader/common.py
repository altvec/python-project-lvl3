# -*- coding: utf-8 -*-

"""Common entities of the project."""
import logging
import os
from functools import wraps

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
            ''.join(err.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
    return res


def create_dir(path):
    """Create directory."""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as err:
            log.exception(''.join(err.args))


def save(path, data, mode='w'):
    """Save provided data."""
    try:
        with open(path, mode) as f:
            f.write(data)
    except IOError as err:
        log.exception(''.join(err.args))


def debug_logger(func):
    """Log decorator function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            log.debug(f'{func.__name__} :: input: {args} {kwargs}')
        log.debug(f'{func.__name__} :: input: {args}')
        result = func(*args, **kwargs)
        log.debug(f'{func.__name__} :: return: {str(result)}')
        return result
    return wrapper
