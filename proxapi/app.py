# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import json
import os
import sys

_here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_here, '..'))

from flask import Flask

from apies import instantiate_apies




def init_app(config=None):
    secrets = json.load(open(os.path.join(_here, '..', 'secrets.json')))

    apies = instantiate_apies(secrets)

    app = Flask(__name__)

    app.config.update(config)

    bootstrap_api_routes(app, apies)

    return app


def bootstrap_api_routes(app, apies):
    '''iterate over all api declarations and register named api endpoints for
    each'''
    for name, api in apies.items():
        route = '/' + name
        app.add_url_rule(route, name, api.dispatcher, methods=['POST'])
