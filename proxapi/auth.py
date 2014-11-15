# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import time
import hashlib
import os
import json

from flask import abort, request
from logbook import info, error


def authentication_required(f, config):
    '''aborts if no valid signature valid in request payload'''
    def decorator(*args, **kwargs):
        if config['DEBUG']:
            # signature not needed in DEBUG mode, continue
            debug('[auth] debug mode => skipping signature validation')
            return f(*args, **kwargs)

        try:
            payload = request.get_json()
            cur_time = int(time.time())
            info('my time: {}'.format(cur_time))
            info('your time: {}'.format(payload['time']))

            # allow for latency of max 2000ms
            for timestamp in xrange(cur_time, cur_time - 3, -1):

                # the order of updates is important
                m = hashlib.sha512()
                m.update(payload['key'])
                m.update(config['app_secret'])
                m.update(str(timestamp))

                if m.hexdigest() == payload['sig']:
                    info('[auth] => valid signature, continue')
                    return f(*args, **kwargs)

        except:
            error('[auth] => could not parse / invalid sig')

            pass

        # we only get here if the sig is invalid or required params were missing
        abort(401)

    return decorator
