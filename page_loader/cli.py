# -*- coding: utf-8 -*-

"""Page loader CLI parser."""

import argparse

from page_loader import logging
from page_loader.downloader import download
from page_loader.logging import configure_logger

parser = argparse.ArgumentParser(description='Page loader')
parser.add_argument('--output', action='store', help='set output dir')
parser.add_argument('url', type=str)
parser.add_argument(
    '--log-level',
    choices=logging.LEVELS,
    default=logging.INFO,
)


def run(args):
    """Run page loader."""
    configure_logger(args.log_level)
    download(args.output, args.url)
