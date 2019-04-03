
import requests
import json

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

def get_edges(after):
    params = {
        "query_hash": query_hash,
        "variables": json.dumps({
            "tag_name":"bakasana",
            "show_ranked": False,
            "first": 7,
            "after": after
        })
    }
    r = requests.get(url, params=params, headers=headers)
    res = r.json()
    edges = res['data']['hashtag']['edge_hashtag_to_media']['edges']
    end_cursor = res['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    return {
        "edges": edges,
        "end_cursor": end_cursor
    }

def image_from_edge(edge):
    return edge['node']['display_url']

first_edges = get_edges(first)
first_end_cursor = first_edges.get('end_cursor')

second_edges = get_edges(first_end_cursor)

first_edge = first_edges.get('edges')[0]
second_edge = second_edges.get('edges')[0]
print(image_from_edge(first_edge))
print(image_from_edge(second_edge))

