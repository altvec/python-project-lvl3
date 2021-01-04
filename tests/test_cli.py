import pytest

from page_loader.cli import parser


@pytest.mark.parametrize('args', (
    ['-o', '/tmp/', 'https://example.com'],
    ['--output', '/tmp/', 'https://example.com'],
    ['-o', '/tmp/', '-l', 'INFO', 'https://example.com'],
    ['-o', '/tmp/', '-l', 'DEBUG', 'https://example.com'],
))
def test_parse_args(args):
    parser.parse_args(args)


@pytest.mark.parametrize('args', (
    [],
    ['https://example.com'],
    ['-o', '/tmp/'],
    ['-o', '/tmp/', '-l', 'DEBUG'],
))
def test_parse_args_raises_for_invalid_args(args):
    with pytest.raises(SystemExit):
        parser.parse_args(args)
