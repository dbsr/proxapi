# -*- coding: utf-8 -*-
# dydrmntion@gmail.com


import hashlib
import time

from proxapi.api import BaseApi, BaseAuth


class RoviAuth(BaseAuth):
    def create_params(self):
        return {
            'apikey': self.key,
            'sig': self._sig()
        }

    def _sig(self):
        timestamp = int(time.time())

        m = hashlib.md5()
        m.update(self.key)
        m.update(self.secret)
        m.update(str(timestamp))

        return m.hexdigest()


class Api(BaseApi):
    _auth = RoviAuth
    default_params = {'format': 'json'}
    base_url = 'http://api.rovicorp.com/data/v1.1'
