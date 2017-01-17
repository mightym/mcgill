#
# Example Settings file for _local_ development.
# This file must not be committed.
#
from .vendor import *

DEBUG = True

SITE_ID = 1

SECRET_KEY = 'totally secret'

ALLOWED_HOSTS = (
    '127.0.0.1',
    'localhost',
    '*', # FIXME
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'db.sqlite3'),
    }
}
