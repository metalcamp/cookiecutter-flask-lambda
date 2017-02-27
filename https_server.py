#!/usr/bin/env python
# -*- coding: utf-8 -*-

from OpenSSL import SSL
from {{cookiecutter.module_name}} import app

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=(
        os.path.join(os.path.dirname(__file__), 'ssl.crt'),
        os.path.join(os.path.dirname(__file__), 'ssl.key')
    ))
