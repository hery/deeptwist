
import ntpath
import requests
import json

from io import BytesIO
from PIL import Image

"""
   Download JSON data containing image URLs through IG's graphQL API.
   query_hash, first, and headers need to be set per session.   
"""


url = 'https://www.instagram.com/graphql/query/'
query_hash = "f92f56d47dc7a55b606908374b43a314"
first = "QVFCR3dNdzBobEZVUnVMTkRWQUNKSTNWdmdyemw0RWktZVB5YkR0ZFAweGV4NWItQnZmdDUyU3Z0dUhGSkdSY0RVU3lxbUFXUUpZbkItZXRCb2NGcnFvSA=="
headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.instagram.com/explore/tags/bakasana/",
    "X-Instagram-GIS": "f9316bbf1af3664ceb284247f7b7d30b",
    "X-IG-App-ID": "936619743392459",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": 'mid=W5DvIAAEAAHAxKrvkh4293IS2CO3; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; shbid=2882; shbts=1554216199.3265219; csrftoken=qYn9WdLPOHjg47lvNSKdEudpqgXNXDH1; ds_user_id=2204414737; sessionid=2204414737%3AyaYnitXJu1SuVo%3A25; rur=ATN; urlgen="{\"217.138.40.54\": 20952}:1hBih1:LV1DhyLYohrwc60pIA_jjx62A7k'
}

ASANA = 'bakasana'

def get_edges(after):
    params = {
        "query_hash": query_hash,
        "variables": json.dumps({
            "tag_name":"bakasana",
            "show_ranked": False,
            "first": 150,
            "after": after
        })
    }
    r = requests.get(url, params=params, headers=headers)
    res = r.json()
    edges = res['data']['hashtag']['edge_hashtag_to_media']['edges']
    print("Receveid %s edges" % len(edges))
    end_cursor = res['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    return {
        "edges": edges,
        "end_cursor": end_cursor
    }

def write_edge(edge, name='00.json'):
    with open(name, 'w') as fp:
        json.dump(edge, fp)

def image_from_edge(edge):
    return edge['node']['display_url']

def get_first_n_batches(n, first=first):
    if n > 0:
        batch = get_edges(first)
        edge = batch.get('edges')
        name = 'data/%s/json/%s.json' % (ASANA, n)
        write_edge(edge, name)
        next_cursor = batch.get('end_cursor')
        get_first_n_batches(n - 1, next_cursor)
    else:
        print('Done')

# first_edges = get_edges(first)
# first_edge = first_edges.get('edges')[0]
# first_image_url = image_from_edge(first_edge)

# res = requests.get(first_image_url)
# image_content = res.content
# i = Image.open(BytesIO(image_content))

# image_name = ntpath.basename(first_image_url)
# query_location = image_name.find('?')
# image_name = image_name[:query_location]
# image_name = 'data/bakasana/%s' % image_name
# print(image_name)

# i.save(image_name)

get_first_n_batches(5)

