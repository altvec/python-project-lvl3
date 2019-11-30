#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Page loader script."""

import argparse

from page_loader.downloader import download


def main():
    """Download and save specified webpage."""
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('--output', action='store', help='set output dir')
    parser.add_argument('webpage', type=str)
    parser.add_argument(
        '--log',
        type=str,
        action='store',
        choices=['all', 'errors', 'nothing'],
        default='nothing',
    )
    args = parser.parse_args()
    download(args.output, args.webpage)


if __name__ == '__main__':
    main()
