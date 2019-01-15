import ntpath
import os
from pathlib import Path
import shutil
import re

import json
import requests


ASANA_KEY = 'bakasana'


def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))


def write_image(display_url, path):
    image = requests.get(display_url, stream=True)
    path += ntpath.basename(display_url)
    if os.path.exists(path):
        return # skip duplicates
    with open(path, 'wb') as f:
        for chunk in image:
            f.write(chunk)


if __name__ == "__main__":
    image_path = "data/%s/images/" % ASANA_KEY
    print("Processing %s...:" % ASANA_KEY)

    # Clean up to prevent duplicates
    print("Cleaning up...")
    purge(image_path, '')

    # Read JSON
    json_path = "data/%s/json/" % ASANA_KEY
    pathlist = Path(json_path).glob('**/*.json')
    for path in pathlist:
        path = str(path)
        data = {}
        with open(path) as f:
            data = json.load(f)

        # Parse JSON and write images
        nodes = data["data"]["hashtag"]["edge_hashtag_to_media"]["edges"]
        print("Fetching %s images..." % len(nodes))
        for node in nodes:
            display_url = node.get("node", {}).get("display_url")
            write_image(display_url, image_path)

    print("Done!")
