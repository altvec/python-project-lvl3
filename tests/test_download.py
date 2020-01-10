# -*- coding: utf-8 -*-

"""Basic tests."""

import os
from tempfile import TemporaryDirectory

import pytest
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

from page_loader.downloader import downloader


def test_download():
    with TemporaryDirectory() as tmpdir:
        expected_file_name = os.path.join(tmpdir, 'example-com.html')
        downloader(tmpdir, 'http://example.com', 'INFO')
        with open(expected_file_name, 'r') as f1:
            actual_content = f1.read()
            with open('./tests/fixtures/example-com.html', 'r') as f2:
                expected_content = f2.read()
                assert actual_content == str(
                    BeautifulSoup(expected_content, 'html.parser').prettify(),
                )


def test_has_local_resources():
    with TemporaryDirectory() as tmpdir:
        downloader(tmpdir, 'https://ru.hexlet.io/pages/about', 'INFO')
        expected_files_dir = os.path.join(
            tmpdir,
            'ru-hexlet-io-pages-about_files',
        )
        assert len(os.listdir(os.path.join(expected_files_dir))) != 0


def test_404_exception():
    with TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://grishaev.me/bookshelf2'
            downloader(tmpdir, url, 'INFO')
        assert '404 Client Error' in str(excinfo.value)


def test_permissions_exception():
    with TemporaryDirectory() as tmpdir:
        os.chmod(tmpdir, 400)
        with pytest.raises(PermissionError) as excinfo:
            url = 'https://hexlet.io/courses'
            downloader(tmpdir, url, 'INFO')
        assert 'Permission denied' in str(excinfo.value)
