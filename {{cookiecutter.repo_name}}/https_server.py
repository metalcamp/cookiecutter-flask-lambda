#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os

from OpenSSL import SSL
from {{cookiecutter.module_name}} import app

CRT_FILE = os.path.join(os.path.dirname(__file__), 'ssl.crt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'ssl.key')

if not os.path.exists(CRT_FILE):
    print("Missing SSL cert file {0}".format(CRT_FILE))
    sys.exit(1)

if not os.path.exists(KEY_FILE):
    print("Missing SSL key file {0}".format(KEY_FILE))
    sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=(CRT_FILE, KEY_FILE))
