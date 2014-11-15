# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import json
import os
import sys

_here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_here, '..'))

from flask import Flask

from apies import instantiate_apies
from auth import authentication_required




def init_app(config=None):
    apies = instantiate_apies(config['secrets'])

    app = Flask(__name__)

    app.config.update(config)

    bootstrap_api_routes(app, apies)

    return app


def bootstrap_api_routes(app, apies):
    '''iterate over all api declarations and register named api endpoints for
    each'''
    for name, api in apies.items():
        route = '/' + name
        decorated = authentication_required(api.dispatcher, app.config)
        app.add_url_rule(route, name, decorated, methods=['POST'])
