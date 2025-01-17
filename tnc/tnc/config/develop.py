import os
from .base import *

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("TNC_DATABASE_NAME"),
        "USER": os.environ.get("TNC_DATABASE_USERNAME"),
        "PASSWORD": os.environ.get("TNC_DATABASE_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

SECRET_KEY = 'django-insecure-ep_095ro+#qcgkgay4t3&b-96$p1esx8ck43!6&9&-xv0z&123'
