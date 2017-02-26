from __future__ import print_function

import re
import sys

# validate the module name
MODULE_NAME = '{{ cookiecutter.module_name }}'
if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9]+$', MODULE_NAME):
    print('ERROR: %s is not a valid Python module name!' % MODULE_NAME)
    sys.exit(1)

# validate the S3 bucket name
S3_BUCKET_NAME = "{{ cookiecutter.s3_bucket_name }}"
if not re.match(r'^[a-z][-.a-z0-9]{2,62}$', S3_BUCKET_NAME):
    print('ERROR: %s is not a valid S3 bucket name!' % S3_BUCKET_NAME)
    sys.exit(1)
