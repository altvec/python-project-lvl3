# -*- coding: utf-8 -*-

"""Basic tests."""

import os

from bs4 import BeautifulSoup
from tempfile import TemporaryDirectory
from page_loader.downloader import download


def test_download():
    with TemporaryDirectory() as tmpdirname:
        expected_file_name = os.path.join(tmpdirname, 'example-com.html')
        actual_file_name = download(tmpdirname, 'http://example.com')
        assert actual_file_name == expected_file_name
        with open(actual_file_name, 'r') as f1:
            actual_content = f1.read()
            with open('./tests/fixtures/example-com.html', 'r') as f2:
                expected_content = f2.read()
                assert actual_content == str(BeautifulSoup(expected_content, 'html.parser').prettify())


def test_has_local_resources():
    with TemporaryDirectory() as tmpdirname:
        expected_file_name = os.path.join(tmpdirname, 'ru-hexlet-io-pages-about.html')
        actual_file_name = download(tmpdirname, 'https://ru.hexlet.io/pages/about')
        expected_files_dir = os.path.join(tmpdirname, 'ru-hexlet-io-pages-about_files')
        assert actual_file_name == expected_file_name
        assert len(os.listdir(os.path.join(expected_files_dir))) != 0
