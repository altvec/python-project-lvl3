#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Page loader script."""

import argparse
import logging
import sys

from page_loader.downloader import downloader


def main():
    """Download and save specified webpage."""
    parser = argparse.ArgumentParser(description='Page loader')
    log_levels = ('INFO', 'DEBUG')
    parser.add_argument('--output', action='store', help='set output dir')
    parser.add_argument('webpage', type=str)
    parser.add_argument(
        '--log-level',
        action='store',
        choices=log_levels,
        default='INFO',
    )
    args = parser.parse_args()

    log_format = '[ %(levelname)s ] %(name)s :: %(message)s'
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        format=log_format,
        level=logging.getLevelName(args.log_level),
    )

    downloader(args.output, args.webpage, args.log_level)


if __name__ == '__main__':
    main()
