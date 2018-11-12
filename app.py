#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask.helpers import get_debug_flag

from tiny_petstore.app import create_app
from tiny_petstore.configs import ProdConfig, DevConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
app.run(port=CONFIG.APP_PORT, debug=CONFIG.DEBUG)
