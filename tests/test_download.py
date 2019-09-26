# -*- coding: utf-8 -*-

"""Basic tests."""

import os

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
                assert actual_content == expected_content