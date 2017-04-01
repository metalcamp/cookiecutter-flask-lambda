# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features (aka Batteries included)

 * [Zappa](https://www.zappa.io) to interact with
 [AWS Lambda](https://aws.amazon.com/lambda/details/)
 * [Flask](http://flask.pocoo.org) is the web application framework
 * [Flask-S3](http://flask-s3.readthedocs.io/en/latest/) is used to manage the
 static assets in S3
 * [Flask SSLify](https://github.com/kennethreitz/flask-sslify) to enforce https.
 * [Pipenv](http://docs.pipenv.org/en/latest/) is used to manage the virtual
 environment and packages.
 * [Boto3](https://boto3.readthedocs.io/en/latest/) to interact with the rest
 of AWS land.
{%- if cookiecutter.add_bootstrap_4 == "y" %}
 * [Bootstrap 4](https://v4-alpha.getbootstrap.com)
{%- endif %}
{%- if cookiecutter.add_jquery_and_turbolinks == "y" %}
 * [Turbolinks](https://github.com/turbolinks/turbolinks)
 * [jQuery](http://jquery.com)
{%- endif %}

## Usage

### Precondition

Python 2.7 is installed and you have setup your
[AWS credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
on your development machine.

### Setup the development environment

The following commands assume that you are working on macOS or any other Unix
environment. [Pipenv](http://docs.pipenv.org/en/latest/) doesn't work on
Windows at the moment.

The first command can be skipped if you have installed
[Pipenv](http://docs.pipenv.org/en/latest/). I strongly
suggest to use python from Homebrew on your macOS machine.

```bash
$ pip install pipenv
$ pipenv install --dev --two
$ pipenv shell
```

### Fire up the local debug server

```bash
$ export FLASK_APP=my_fancy_new_project_name
$ export FLASK_DEBUG=1
$ flask run
```

### Deploy the project

```bash
$ zappa deploy
```

### Undeploy the project

```bash
$ zappa undeploy
```

{%- if cookiecutter.use_mit_license == "y" %}
## License

"{{ cookiecutter.project_name }}" is licensed under the MIT license. For more
information see LICENSE.
{%- endif %}

## Changelog

### {{ cookiecutter.version }}

 * Initial release.

## Contributors

 * {{ cookiecutter.full_name }}
