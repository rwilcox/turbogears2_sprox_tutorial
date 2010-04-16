# -*- coding: utf-8 -*-
"""Setup the turbogears2-sprox-tutorial application"""

import logging
from tg import config
from turbogears2_sprox_tutorial import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup turbogears2_sprox_tutorial here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
