# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="{{ cookiecutter.module_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Operating System :: OS Independent",
    ],
    packages=["{{ cookiecutter.module_name }}"],
    include_package_data=True,
    install_requires=[
        "flask >= 0.12",
        "flask-s3 >= 0.3",
        "zappa >= 0.35",
        "boto3 >= 1.4"
    ],
)
