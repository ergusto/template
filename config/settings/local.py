import os
from .base import *

DEBUG = True

SECRET_KEY = "{{ secret_key }}"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "{{ project_name }}",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "build/",
        "STATS_FILE": os.path.join(PROJECT_DIR, "client/webpack/stats.local.json"),
    }
}
