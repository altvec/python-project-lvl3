#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Page loader script."""

import asyncio
import logging
import sys
from pathlib import Path

from page_loader.cli import parser
from page_loader.loader import download
from page_loader.logging import configure_logger


def main():
    """Download and save specified webpage."""
    args = parser.parse_args()

    configure_logger(args.log_level)
    log = logging.getLogger(__name__)

    try:
        asyncio.run(download(args.url, Path(args.output)))
    except Exception as e:
        log.error(e)
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
