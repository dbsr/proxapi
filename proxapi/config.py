# -*- coding: utf-8 -*-
# dydrmntion@gmail.com


import os


config = dict(
    DEBUG=os.environ.get('USER') == 'dbsr',
    lastfm=dict(
        key=os.environ['LASTFM_KEY'],
        secret=os.environ['LASTFM_SECRET']),
    rovi=dict(
        key=os.environ['ROVI_KEY'],
        secret=os.environ['ROVI_SECRET']),
    app_secret=os.environ['APP_SECRET'])
