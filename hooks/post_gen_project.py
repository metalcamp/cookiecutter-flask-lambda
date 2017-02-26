#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if "{{ cookiecutter.build_alexa_skill }}" != "y":
    os.unlink(os.path.join("{{ cookiecutter.module_name }}", "templates.yaml"))
    os.unlink(os.path.join("{{ cookiecutter.module_name }}", "intents.py"))
