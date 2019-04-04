
from io import BytesIO
import json
from pathlib import Path
import ntpath
import requests
from PIL import Image


ASANA = 'bakasana'


def download_and_save_image(url):
    res = requests.get(url)
    img_content = res.content
    i = Image.open(BytesIO(img_content))
    img_name = ntpath.basename(url)
    query_location = img_name.find('?')
    img_name = img_name[:query_location]
    img_path = 'data/%s/%s' % (ASANA, img_name)
    i.save(img_path)


def read_batches():
    json_path = "data/%s/json/" % ASANA
    pathlist = Path(json_path).glob('**/*.json')
    for path in pathlist:
        path = str(path)
        with open(path) as fp:
            data = json.load(fp)
            parse_edges(data)


def parse_edges(data):
    for edge in data:
        node = edge.get('node')
        display_url = node.get('display_url')
        download_and_save_image(display_url)


read_batches()
