import os
import dj_database_url
from .base import *

DEBUG = os.environ.get('DJANGO_DEBUG', False) == "True"

DATABASES['default'] = dj_database_url.config()
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += ('storages',)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(PROJECT_DIR, os.pardir, 'static')
# Use Amazon S3 for storage for uploaded media files.
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Amazon S3 settings.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_AUTO_CREATE_BUCKET = False
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = True
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False

MEDIA_ROOT = '/'
MEDIA_URL = '//s3.amazonaws.com/{}/'.format(AWS_STORAGE_BUCKET_NAME)
