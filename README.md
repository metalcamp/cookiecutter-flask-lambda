# cookiecutter-flask-lambda

A simple [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template to create a web application or an Alexa Skill that is deployed on
[AWS Lambda](https://aws.amazon.com/lambda/details/) using
[Zappa](https://www.zappa.io) and [Flask](http://flask.pocoo.org). The
resulting project is using [Pipenv](http://docs.pipenv.org/en/latest/) to
manage its virtual environment and packages.

## Usage

```bash
$ pip install cookiecutter pipenv
$ cookiecutter https://github.com/oa/cookiecutter-flask-lambda.git
$ cd my-fancy-new-project-name
$ pipenv install --dev --two
$ pipenv shell
$ pip install -e .
```

You will be asked about your basic info (name, project name, repo name, etc.).
This info will be used in your new project. Afterwards you are ready to fire up
the local debugging server and start developing your application.

```bash
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
 * [normalize.css](https://necolas.github.io/normalize.css/) if you don't
 include Bootstrap 4 (See below).
 * It uses the layout for
 [larger flask applications](http://flask.pocoo.org/docs/0.12/patterns/packages/).
 Mainly, because I prefer a little bit more structure in my projects.

### Optional Features

 * Add [Flask-Ask](https://github.com/johnwheeler/flask-ask) to your project to
 develop Alexa skills. This also adds a Python file with the demo memory game
 taken from a
 [tutorial](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)
 posted on AWS developer blog.
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

### 0.2.1

 * Bugfixing Alexa demo app. Added a missing import.

### 0.2.0

 * Added optional support for Bootstrap 4, Turbolinks or jQuery.
 * Added optional Flask-Ask aka Alexa Skill support.

### 0.1.0

 * Initial release.

## Contributors

 * Oliver Andrich
