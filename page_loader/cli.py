# -*- coding: utf-8 -*-

"""Page loader CLI parser."""

import argparse


def parse_args():
    """Parse CLI arguments."""
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
    return parser.parse_args()
