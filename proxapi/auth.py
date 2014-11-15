# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import time
import hashlib
import os
import json

from flask import abort, request


def authentication_required(f, config):
    '''aborts if no valid signature valid in request payload'''
    def decorator(*args, **kwargs):
        if config['DEBUG']:
            # signature not needed in DEBUG mode, continue
            return f(*args, **kwargs)

        try:
            payload = request.get_json()

            # the order of updates is important
            m = hashlib.sha512()
            m.update(payload['key'])
            m.update(config['app_secret'])
            m.update(str(int(time.time())))

            if m.hexdigest() == payload['sig']:
                return f(*args, **kwargs)

        except:
            pass

        # we only get here if the sig is invalid or required params were missing
        abort(401)

    return decorator
