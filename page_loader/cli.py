# -*- coding: utf-8 -*-

"""Page loader CLI parser."""

import argparse

from page_loader import logging

parser = argparse.ArgumentParser(description='Page loader')
parser.add_argument('url', type=str)
parser.add_argument(
    '-o',
    '--output',
    type=str,
    required=True,
    help='set output directory',
)
parser.add_argument(
    '-l',
    '--log-level',
    choices=logging.LEVELS,
    default=logging.INFO,
    help='set log level',
)
