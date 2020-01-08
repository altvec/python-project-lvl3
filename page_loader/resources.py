# -*- coding: utf-8 -*-

"""Local resources."""
import logging
import os

from progress.bar import Bar

from page_loader.common import LOCAL_RESOURCES, create_dir, get_url, save
from page_loader.names import create_resource_name

log = logging.getLogger(__name__)


def download_resources(resources, base_url, resources_dir_name):
    """Download local resources."""
    create_dir(resources_dir_name)
    total_size = len(resources)
    with Bar('Downloading', max=total_size) as bar:
        for r, _ in zip(resources, range(total_size)):
            url = f'{base_url}/{r["old_value"]}'
            path = os.path.join(resources_dir_name, r['new_value'])
            save(path, get_url(url).content, 'wb')
            bar.next()


def find_resources(soup, path):
    """Find local resources and replace paths in soup object."""
    resources = []
    for tag, attr in LOCAL_RESOURCES.items():
        for item in soup.find_all(tag):
            attr_val = item.get(attr)
            if attr_val is not None and attr_val.startswith('/'):
                base, ext = os.path.splitext(attr_val)
                if ext != '':
                    new_attr_val = create_resource_name(attr_val)
                    resources.append(
                        {
                            'old_value': attr_val,
                            'new_value': new_attr_val,
                        },
                    )
                    item[attr] = os.path.join(
                        path,
                        new_attr_val,
                    )
    return (soup, resources)
