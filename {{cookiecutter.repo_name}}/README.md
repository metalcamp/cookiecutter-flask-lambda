# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Batteries included

This project uses [Zappa](https://www.zappa.io) to interact with
[AWS Lambda](https://aws.amazon.com/lambda/details/).
[Flask](http://flask.pocoo.org) is the web application framework of choice in
this project. And [Pipenv](http://docs.pipenv.org/en/latest/) is used to
manage the virtual environment and packages. See the Pipfile
for more details.

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
$ pip install -e .
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

## License

"{{ cookiecutter.project_name }}" is licensed under the MIT license. For more
information see LICENSE.

## Changelog

### {{ cookiecutter.version }}

 * Initial release.

## Contributors

 * {{ cookiecutter.full_name }}
