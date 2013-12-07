'''
Client for the item endpoint API.

Optionally a requests session can be provided in order to leave the connection
open between subsequent requests.
'''
import requests
import json


def _do_request(method, url, session=None, **kwargs):
    client = session if session is not None else requests
    resp = client.request(method, url, **kwargs)
    resp.raise_for_status()
    try:
        return resp.json()
    except ValueError:
        return resp.content


def get_item(url, key, session=None):
    return _do_request('GET', 'http://{}/item/{}/'.format(url, key),
                       session=session)


def get_items(url, session=None):
    return  _do_request('GET', 'http://{}/item/'.format(url),
                        session=session)


def post_item(url, key, value, session=None):
    payload = { "key": key, "value": value }
    return _do_request('POST', 'http://{}/item/'.format(url),
                       session=session, data=payload)


def delete_items(url, session=None):
    data = get_items(url)
    for item in data:
        _do_request('DELETE', "http://{}/item/{}/".format(url, item['key']),
                    session=session)
