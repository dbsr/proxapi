# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import requests
from flask import request, jsonify


class BaseAuth(object):
    def __init__(self, key, secret, *args, **kwargs):
        self.key = key
        self.secret = secret

    def __call__(self, r):
        params = self.create_params()

        r.prepare_url(r.url, params)

        return r

    def create_params(self):
        return {}



class BaseApi(object):
    _auth = BaseAuth
    def __init__(self, *args, **kwargs):
        session = requests.Session()

        if self._auth:
            auth = self._auth(*args, **kwargs)
            session.auth = auth

        self.session = session

    def make_request(self, resource=None, params=None):
        if resource is None:
            resource = ''
        if params is None:
            params = {}

        # set default params
        params.update(self.default_params)

        url = self.base_url + '/' + resource

        r = self.session.get(url=url, params=params)

        try:
            r.raise_for_status()
        except:
            return None

        return r

    def dispatcher(self):
        '''simple dispatch proxy converting json data to arguments for 
        the actual api proxy handler'''
        try:
            resp = self.get(**request.get_json())
        except Exception as e:
            return jsonify(dict(
                error=e.message)), 400
        return jsonify(resp)
            

    def get(self, resource=None, params=None, *args, **kwargs):

        '''make a GET request using provided resource and params.
        Optional mappings will be used to get specific parts of the 
        JSON response.'''
        if not resource:
            resource = ''
        if not params:
            params = {}

        resp = self.make_request(resource, params)
        json_response = resp.json()

        return json_response
