# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import json

from proxapi.app import init_app


secrets = json.load(open('secrets.json'))

config = dict(
    DEBUG=True,
    SERVER_NAME='localhost:9999',
    secrets=secrets)

app = init_app(config)

app.run()
