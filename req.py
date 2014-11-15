#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import json
import hashlib
import time
import os

import requests

TEST_APIKEY = '1234abcd1234abcd'

secret = os.environ['APP_SECRET']
print secret

def create_sig(apikey):
    sha = hashlib.sha512()
    sha.update(apikey)
    sha.update(secret)
    sha.update(str(int(time.time())))

    return sha.hexdigest()


def req(api, payload):

    url = 'http://proxapi.herokuapp.com/' + api
    payload.update(dict(
        key=TEST_APIKEY,
        sig=create_sig(TEST_APIKEY)))
    headers = {'content-type': 'application/json'}

    req = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        resp = req.json()
    except:
        resp = req.content

    return resp


if __name__ == '__main__':
    import sys
    api = sys.argv[1]
    fpath = sys.argv[2] if len(sys.argv) > 2 else 'payload.json'
    payload = json.load(open(fpath))

    print req(api, payload)
