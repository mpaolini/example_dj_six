'''
Client for the item endpoint API.

Optionally a requests session can be provided in order to leave the connection
open between subsequent requests.
'''
import requests
import json
from .models import Item

def get_item(url, key, session=None):
    if session is None:
        r = requests.get("http://{}/{}/{}/".format(url, "item", key))
    else:
        r = session.get("http://{}/{}/{}/".format(url, "item", key))
    return r.text

def get_items(url, session=None):
    if session is None:
        r = requests.get("http://{}/{}/".format(url, "item"))
    else:
        r = session.get("http://{}/{}/".format(url, "item"))
    return r.text

def post_item(url, key, value, session=None):
    payload = { "key": key, "value": value }
    if session is None:
        requests.post("http://{}/{}/".format(url, "item"), data=payload)
    else:
        session.post("http://{}/{}/".format(url, "item"), data=payload)

def delete_items(url, session=None):
    j = get_items(url)
    objs = json.loads(j)
    for item in objs:
        _url = "http://{}/{}/{}/".format(url, "item", item['key'])
        if session is None:
            requests.delete(_url)
        else:
            session.delete(_url)
