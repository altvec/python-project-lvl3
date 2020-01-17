# -*- coding: utf-8 -*-

"""Basic tests."""

import os
from tempfile import TemporaryDirectory

import pytest
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

from page_loader.downloader import download


def read_file(path):
    with open(path) as f:
        return f.read()


def test_download():
    with TemporaryDirectory() as tmpdir:
        download(tmpdir, 'http://example.com')
        actual = read_file(os.path.join(tmpdir, 'example-com.html'))
        expected = read_file('./tests/fixtures/example-com.html')
        assert actual == expected


def test_has_local_resources():
    with TemporaryDirectory() as tmpdir:
        download(tmpdir, 'https://ru.hexlet.io/pages/about')
        expected = os.path.join(
            tmpdir,
            'ru-hexlet-io-pages-about_files',
        )
        assert len(os.listdir(os.path.join(expected))) != 0


def test_404_exception():
    with TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://grishaev.me/bookshelf2'
            download(tmpdir, url)
        assert '404 Client Error' in str(excinfo.value)


def test_permissions_exception():
    with TemporaryDirectory() as tmpdir:
        os.chmod(tmpdir, 400)
        with pytest.raises(PermissionError) as excinfo:
            url = 'https://hexlet.io/courses'
            download(tmpdir, url)
        assert 'Permission denied' in str(excinfo.value)
