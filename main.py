import shutil
import ntpath

import json
import requests

# Read JSON
data = {}
with open("data/bakasana/json/00.json") as f:
    data = json.load(f)

# Parse JSON
node = data["data"]["hashtag"]["edge_hashtag_to_media"]["edges"][0]["node"]
display_url = node["display_url"]

# Write image
image = requests.get(display_url, stream=True)
path = "data/bakasana/images/"
path += ntpath.basename(display_url)
with open(path, 'wb') as f:
    for chunk in image:
        f.write(chunk)
