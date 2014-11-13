# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import time
import hashlib
import os
import json

from flask import abort, request



_here = os.path.dirname(os.path.realpath(__file__))

secrets = json.load(open(os.path.join(_here, '..', 'secrets.json')))


def authentication_required(f):
    '''aborts if no valid signature valid in request payload'''
    def decorator(*args, **kwargs):
        try:
            payload = request.get_json()

            m = hashlib.md5()
            m.update(str(int(time.time())))
            m.update(secrets['secret'])
            m.update(payload['key'])

            if m.hexdigest() == payload['sig']:
                return f(*args, **kwargs)

        except:
            pass

        abort(401)

    return decorator
