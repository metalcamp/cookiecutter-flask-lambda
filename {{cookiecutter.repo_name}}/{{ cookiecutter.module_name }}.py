# -*- coding: utf-8 -*-
from __future__ import print_function

import logging

from flask import Flask, render_template
from flask_s3 import FlaskS3
from flaskext.markdown import Markdown
from flask_sslify import SSLify

# SETUP FLASK APPLICATION -----------------------------------------------------

app = Flask(__name__)

# configure Flask-S3 support
app.config["FLASKS3_BUCKET_NAME"] = "{{ cookiecutter.s3_bucket_name }}"
app.config["FLASKS3_BUCKET_DOMAIN"] = "s3-{{ cookiecutter.aws_region }}.amazonaws.com"
app.config["FLASKS3_URL_STYLE"] = "path"
app.config["FLASKS3_FORCE_MIMETYPE"] = True
FlaskS3(app)

def upload_static_assets(cli):
    """Helper function to upload the static assets to S3 in production mode."""
    import flask_s3
    flask_s3.create_all(app)

# add the filter from Flask-Markdown
Markdown(app, extensions=['fenced_code'])

# VIEWS -----------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("base.html", content=open("README.md").read())

# CLI INTERFACE ---------------------------------------------------------------


