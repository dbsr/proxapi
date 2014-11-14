# -*- coding: utf-8 -*-
# dydrmntion@gmail.com

import os
import imp
import sys

_here = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(_here, '..'))


def instantiate_apies(secrets):
    apies = {}

    # assume every directory here is an api declaration
    for api in os.listdir(_here):
        if api.endswith('.py') and not api.startswith('_'):
            name = api.strip('.py')
            fpath = os.path.join(_here, api)
            module = imp.load_source(name, fpath)
            apies[name] = module.__dict__['Api'](**secrets.get(name, {}))

    return apies
