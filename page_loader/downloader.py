# -*- coding: utf-8 -*-

"""Main logic module."""

import os
from urllib.parse import urlparse

import requests


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
    file_path = os.path.join(output_path, file_name)
    with open(file_path, 'w') as f:
        f.write(content)
    return file_path
