# -*- coding: utf-8 -*-

"""Main logic module."""

import os
from urllib.parse import urlparse

import requests


def save_page(file_path, content):
    """Save data into path."""
    output_dir, file_name = file_path
    path = os.path.join(output_dir, file_name)
    with open(path, 'w') as f:
        f.write(content)
    return path


def generate_file_name(url):
    """Generate filename."""
    parsed_url = urlparse(url)
    host = parsed_url.netloc.replace('.', '-')
    document = parsed_url.path.replace('/', '-')
    file_name = host + document + '.html'
    return file_name


def download(output_path, webpage):
    """Download page and save into path."""
    file_name = generate_file_name(webpage)
    content = requests.get(webpage).text
    return save_page((output_path, file_name), content)
