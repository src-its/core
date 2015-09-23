from .includes.common import *

DEBUG = True

# Make these unique, and don't share it with anybody.
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "its_staging",
        "USER": "its",
        "PASSWORD": DBPASSWORD,
        "HOST": "",
        "PORT": ""}}

AWS_STORAGE_BUCKET_NAME = "src-its-secure"

POSTGIS_VERSION = (2, 1, 2)

###################
# DEPLOY SETTINGS #
###################

GUNICORN_BIND = "127.0.0.1:8200"
PROCESS_USER = 'its'
PROCESS_NAME = 'its_staging'
SITE_TITLE = 'SRC-ITS Staging'
SITE_TAGLINE = None
VIRTUALENV = 'src-its'
