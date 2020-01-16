#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Page loader script."""

import sys

from page_loader import cli


def main():
    """Download and save specified webpage."""
    try:
        cli.run(cli.parser.parse_args())
    except Exception as e:
        if 'url' in str(e.args):
            sys.exit(1)
        elif 'Permission denied' in str(e.args):
            sys.exit(2)
    sys.exit(0)


if __name__ == '__main__':
    main()
