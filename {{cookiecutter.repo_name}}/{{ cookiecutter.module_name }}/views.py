# -*- coding: utf-8 -*-

from flask import render_template
from {{cookiecutter.module_name}}.application import app


@app.route("/")
def index():
    return render_template("base.html", content=open("README.md").read())
