# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import sys
import os

# first add the api declaration module to our path
_here = os.path.join(os.path.realpath(__file__), '..')
sys.path.append(os.path.join(_here, '..'))

from apies import apies


def bootstrap_api_routes(app):
    '''iterate over all api declarations and register named api endpoints for 
    each'''
    for name, api in apies.items():
        route = '/' + name
        app.add_url_rule(route, name, api.dispatcher, methods=['POST'])
