# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

from proxapi.api import BaseAuth, BaseApi



class LastFmAuth(BaseAuth):
    def create_params(self):
        return {
            'api_key': self.key,
            'secret': self.secret
        }


class Api(BaseApi):
    _auth = LastFmAuth
    default_params = {'format': 'json'}
    base_url = 'http://ws.audioscrobbler.com/2.0/'
