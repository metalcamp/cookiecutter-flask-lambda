# cookiecutter-flask-lambda

A simple [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template to create a web application that is deployed on
[AWS Lambda](https://aws.amazon.com/lambda/details/) using
[Zappa](https://www.zappa.io) and [Flask](http://flask.pocoo.org). The
resulting project is using [Pipenv](http://docs.pipenv.org/en/latest/) to
manage its virtual environment and packages.

## Usage

```
$ pip install cookiecutter pipenv
$ cookiecutter https://github.com/oliverandrich/cookiecutter-flask-lambda.git
$ cd my-fancy-new-project-name
$ pipenv install --dev --two
$ pipenv shell
```

You will be asked about your basic info (name, project name, repo name, etc.).
This info will be used in your new project. Afterwards you are ready to fire up
the local debugging server and start developing your application.

```
$ export FLASK_APP=my_fancy_new_project_name
$ export FLASK_DEBUG=1
$ flask run
```

**Enjoy!**

## Features (aka Batteries included)

 * Includes you need to build and deploy an app on
 [AWS Lambda](https://aws.amazon.com/lambda/details/)
    * [Zappa](https://www.zappa.io)
    * [Flask](http://flask.pocoo.org)
    * [Boto3](https://boto3.readthedocs.io/en/latest/)
    * [awscli](https://github.com/aws/aws-cli)
 * Uses [Pipenv](http://docs.pipenv.org/en/latest/) to manage the virtual
 environment and packages.
 * [pytest](http://doc.pytest.org/en/latest/) and
 [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/) are included to
 ease the testing of your application.
 * [Flask-S3](http://flask-s3.readthedocs.io/en/latest/) to easily serve the
 static assets of your Flask application from your S3 bucket.
 * [Flask-SSLify](https://github.com/kennethreitz/flask-sslify) - we all prefer
 HTTPS these days, don't we. SSLify is activated only in production mode.
 * [normalize.css](https://necolas.github.io/normalize.css/) if you don't
 include Bootstrap 4 (See below).

### Optional Features

 * Add [Turbolinks](https://github.com/turbolinks/turbolinks)
 and [jQuery](http://jquery.com) to your project. For some simpler projects I
 still prefer these trusted tools.
 * Add [Bootstrap 4](https://v4-alpha.getbootstrap.com) to your project.

## License

cookiecutter-flask-lambda is licensed under the MIT license. For more
information see LICENSE.

## TODOs

 * Add support for Travis CI to the cookiecutter recipe and the project template.

## Changelog

### 0.7.0

 * Zappa 0.41 is the new minimum version.
 * Python 3.6 is the default runtime.
 * Kicked Bootstrap.
 * Kicked Turbolinks.
 * Added materialize.css as an option.
 * Added intercooler.js as an option.

### 0.6.0

 * MIT License can be removed from the new project.

### 0.5.0

 * Stripped Flask-Ask support. Moved the Alexa stuff to a seperate and simpler cookiecutter template.
 * Moved to the simple default layout of Flask apps.

### 0.4.2

 * Bugfixes for https_server.py.
 * Updates to this file and the README.md of the project template.

### 0.4.1

 * Bugfixes to the default intents file for Alexa skills.

### 0.4.0

 * Added Flask-SSLify.

### 0.3.1

 * Bugfix for instantiating Flask-Ask.

### 0.3.0

 * Added a simple script to start a local HTTPS server - https_server.py. It
 expects a file ssl.cert and ssl.key in your project root.

### 0.2.1

 * Bugfixing Alexa demo app. Added a missing import.

### 0.2.0

 * Added optional support for Bootstrap 4, Turbolinks or jQuery.
 * Added optional Flask-Ask aka Alexa Skill support.

### 0.1.0

 * Initial release.

## Contributors

 * Oliver Andrich
