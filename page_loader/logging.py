# -*- coding: utf-8 -*-

"""Logging configuration."""

import logging
import sys


def configure_logger(log_level):
    """Configure app logging."""
    log_format = '[ %(levelname)s ] %(name)s :: %(message)s'
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        format=log_format,
        level=logging.getLevelName(log_level),
    )
