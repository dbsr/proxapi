# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import requests
from flask import request, jsonify
from logbook import debug, info, warn, error


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
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.log(info, 'initiating api')

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

        self.log(info,
            "request initiating with resource: '{}' and params: '{}'".format(
                resource, repr(params)))

        # set default params
        params.update(self.default_params)

        url = self.base_url + '/' + resource

        r = self.session.get(url=url, params=params)

        try:
            r.raise_for_status()
        except:
            self.log(error, 'request failed with status_code: {}'.format(
                r.status_code))
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

        # make sure the response is 'jsonifyable'
        response = dict(response=resp)

        return jsonify(response)


    def get(self, resource=None, params=None, mappings=None, *args, **kwargs):
        '''make a GET request using provided resource and params.
        Optional mappings will be used to get specific parts of the
        JSON response.'''
        if not resource:
            resource = ''
        if not params:
            params = {}

        resp = self.make_request(resource, params)
        json_response = resp.json()

        if mappings:
                json_response = self.get_mapped_response(json_response, mappings)

        return json_response

    def get_mapped_response(self, response, mappings):
        '''uses the list of mappings to traverse a nested json response'''
        for mapping in mappings:
            if isinstance(mapping, list):
                # assume we need to return a subset of results using this
                # mappings items as keys on each subset
                return [dict((key, item[key]) for key in mapping) for item in response]

            response = response.get(mapping)

        return response

    def log(self, level, message):
        level('[{:>4}] {}'.format(self.name, message))
