# -*- coding: utf-8 -*-

"""Main logic module."""

import os

import requests
from bs4 import BeautifulSoup

from page_loader.constants import LOCAL_RESOURCES
from page_loader.gen_name import generate_name
from page_loader.parse_url import parse_url


def create_dir(path):
    """Create directory."""
    if not os.path.exists(path):
        os.makedirs(path)


def save_file(path, data, mode='w'):
    """Save file to specified path."""
    with open(path, mode) as f:
        f.write(data)


def download_resources(path, resources, output):
    """Download local resources."""
    for r in resources:
        file_name = generate_name(r)
        data = requests.get(path + r).content
        save_file(join_paths(output, file_name), data, 'wb')


def get_local_resources(content, files_path):
    """Get local resources from webpage."""
    res = []
    for tag, attr in LOCAL_RESOURCES.items():
        for item in content.find_all(tag):
            attr_value = item.get(attr)
            if attr_value is not None and is_local(attr_value):
                res.append(attr_value)
                item[attr] = join_paths(files_path, generate_name(attr_value))
    return (res, content)


def is_local(resource):
    """Check if resource is local (means it doesn't have host in it)."""
    hostname, _ = parse_url(resource)
    return hostname == ''


def join_paths(path, filename):
    """Join path and filename."""
    return os.path.join(path, filename)


def download(output_path, url):
    """Download page and its local resources and save to specified path."""
    page_name = generate_name(url)
    page_path = join_paths(output_path, page_name + '.html')
    files_path = join_paths(output_path, page_name + '_files')
    resources, page = get_local_resources(
        BeautifulSoup(requests.get(url).text, 'html.parser'),
        files_path,
    )

    create_dir(files_path)
    save_file(page_path, str(page.prettify()))
    download_resources(url, resources, files_path)

    return page_path
