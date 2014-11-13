# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

from proxapi.app import init_app



config = dict(
    DEBUG=True,
    SERVER_NAME='localhost:9999')

app = init_app(config)

app.run()
