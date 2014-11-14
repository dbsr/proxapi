# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

from proxapi.api import BaseApi


class Api(BaseApi):
    _auth = None
    default_params = {'r': 'json'}
    base_url = 'http://www.omdbapi.com/'
