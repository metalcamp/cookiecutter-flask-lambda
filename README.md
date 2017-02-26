# cookiecutter-flask-lambda

A simple [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template to create a web application that is deployed on
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
 * It uses the layout for
 [larger flask applications](http://flask.pocoo.org/docs/0.12/patterns/packages/).
 Mainly, because I prefer a little bit more structure in my projects.

## License

cookiecutter-flask-lambda is licensed under the MIT license. For more
information see LICENSE.

## TODOs

 * Add support for Travis CI to the cookiecutter recipe and the project template.

## Changelog

### 0.1.0

 * Initial release.

## Contributors

 * Oliver Andrich
