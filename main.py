import ntpath
import os
from pathlib import Path
import shutil
import re
import sys

import json
import requests


# We can get unique images by chaining the end_cursor as the after parameter of the next GraphQL request

# 10 classes like CIFAR-10
ASANA_KEYS = [
    'tadasana',
    'urdhvahastasana',
    'uttanasana',
    'chaturangadandasana',
    'urdhvamukhasvanasana',
    'adhomukhasvanasana',
    'utkatasana',
    'virabhadrasana1',
    'virabhadrasana2',
    'bakasana',
]


ASANA_KEY = 'virabhadrasana1' # deprecated


def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

def build_dirs(asana_keys):
    for asana_key in asana_keys:
        class_path = 'data/%s/json' % asana_key
        if not os.path.exists(class_path):
            os.makedirs(class_path)
            # touch(class_path + '/curl.sh')


def write_image(display_url, path):
    image = requests.get(display_url, stream=True)
    path += ntpath.basename(display_url)
    if os.path.exists(path):
        return # skip duplicates
    with open(path, 'wb') as f:
        for chunk in image:
            f.write(chunk)


if __name__ == "__main__":

    build_dirs(ASANA_KEYS)


    # image_path = "data/%s/images/" % ASANA_KEY
    # print("Processing %s...:" % ASANA_KEY)

    # Clean up to prevent duplicates
    # print("Cleaning up...")
    # purge('data/', '')

    # # Read JSON
    # json_path = "data/%s/json/" % ASANA_KEY
    # pathlist = Path(json_path).glob('**/*.json')
    # for path in pathlist:
    #     path = str(path)
    #     data = {}
    #     with open(path) as f:
    #         data = json.load(f)

    #     # Parse JSON and write images
    #     nodes = data["data"]["hashtag"]["edge_hashtag_to_media"]["edges"]
    #     print("Fetching %s images..." % len(nodes))
    #     for node in nodes:
    #         display_url = node.get("node", {}).get("display_url")
    #         write_image(display_url, image_path)

    print("Done!")
