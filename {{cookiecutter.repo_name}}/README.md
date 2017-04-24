# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Usage

### Precondition

Python 3.6 is installed and you have setup your
[AWS credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
on your development machine.

### Setup the development environment

```bash
$ pip install pipenv
$ pipenv install --dev --three
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
