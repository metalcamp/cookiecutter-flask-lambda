# -*- coding: utf-8 -*-

import logging

from flask import Flask
from flask_s3 import FlaskS3
from flaskext.markdown import Markdown
from flask_ask import Ask

# setup the basic Flask app
app = Flask(__name__)

# configure Flask-S3 support
app.config["FLASKS3_BUCKET_NAME"] = "{{ cookiecutter.s3_bucket_name }}"
app.config["FLASKS3_BUCKET_DOMAIN"] = "s3-{{ cookiecutter.aws_region }}.amazonaws.com"
app.config["FLASKS3_URL_STYLE"] = "path"
app.config["FLASKS3_FORCE_MIMETYPE"] = True
FlaskS3(app)

# add the filter from Flask-Markdown
Markdown(app, extensions=['fenced_code'])

{%- if cookiecutter.build_alexa_skill == "y" %}
# configure the Ask (aka Alexa) support
ask = Ask(app, "{{ cookiecutter.module_name }}")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

import {{cookiecutter.module_name}}.intents
{%- endif %}

import {{cookiecutter.module_name}}.views


def upload_static_assets(cli):
    import flask_s3
    flask_s3.create_all(app)
