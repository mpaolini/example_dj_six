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
        r = requests.get("http://%s/%s/%d/" % (url, "item", key))
    else:
        r = session.get("http://%s/%s/%d/" % (url, "item", key))
    return r.text

def get_items(url, session=None):
    if session is None:
        r = requests.get("http://%s/%s/" % (url, "item"))
    else:
        r = session.get("http://%s/%s/" % (url, "item"))

    return r.text

def post_item(url, key, value, session=None):
    payload = { "key": key, "value": value }
    if session is None:
        r = requests.post("http://%s/%s/" % (url, "item"), data=payload)
    else:
        r = session.post("http://%s/%s/" % (url, "item"), data=payload)

def delete_items(url, session=None):
    j = get_items(url)
    objs = json.loads(j)
    for item in objs:
        _url = "http://%s/%s/%s/" % (url, "item", item['key'])
        if session is None:
            r = requests.post(_url, headers={'X-HTTP-Method-Override': 'DELETE'})
        else:
            r = session.post(_url, headers={'X-HTTP-Method-Override': 'DELETE'})
