# -*- coding: utf-8 -*-

"""Basic tests."""

import asyncio
import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from page_loader.cli import parser
from page_loader.exceptions import LoadingError
from page_loader.loader import download


def read_file(path):
    with open(path) as f:
        return f.read()


@pytest.mark.asyncio
async def test_download():
    with TemporaryDirectory() as tmpdir:
        await download('http://example.com', Path(tmpdir))
        actual = read_file(os.path.join(tmpdir, 'example-com.html'))
        expected = read_file('./tests/fixtures/example-com.html')
        assert actual == expected


@pytest.mark.asyncio
async def test_has_local_resources():
    with TemporaryDirectory() as tmpdir:
        await download('https://clojure.org', Path(tmpdir))
        expected = os.path.join(
            tmpdir,
            'clojure-org_files',
        )
        assert len(os.listdir(os.path.join(expected))) != 0


@pytest.mark.asyncio
async def test_404_exception():
    with TemporaryDirectory() as tmpdir:
        with pytest.raises(LoadingError) as excinfo:
            url = 'https://clo.fdd'
            await download(url, Path(tmpdir))
        assert 'HTTP client error' in str(excinfo.value)


@pytest.mark.asyncio
async def test_permissions_exception():
    with TemporaryDirectory() as tmpdir:
        os.chmod(tmpdir, 400)
        with pytest.raises(PermissionError) as excinfo:
            url = 'https://hexlet.io/courses'
            await download(url, Path(tmpdir))
        assert 'Permission denied' in str(excinfo.value)
