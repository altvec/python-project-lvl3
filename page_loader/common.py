# -*- coding: utf-8 -*-

"""Common entities of the project."""

import logging
from functools import wraps

log = logging.getLogger(__name__)

LOCAL_RESOURCES = {  # noqa: 407
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def debug_logger(func):
    """Log decorator function.

    Args:
        func: function, that will be decorated

    Returns:
        function-wrapper around decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):  # noqa: WPS430
        func_name = f'[{func.__name__:>30}]'

        log.debug(f'{func_name} :: input: {args} {kwargs}')
        res = func(*args, **kwargs)
        log.debug(f'{func_name} :: return: {str(res)}')
        return res
    return wrapper
