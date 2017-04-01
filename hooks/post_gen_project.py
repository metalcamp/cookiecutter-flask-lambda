#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if "{{ cookiecutter.use_mit_license }}".lower() != "y":
    os.unlink(os.path.join(PROJECT_DIRECTORY, "LICENSE"))

