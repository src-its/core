from .includes.common import *

DEBUG = True

# Make these unique, and don't share it with anybody.
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "its",
        "USER": "its",
        "PASSWORD": "src-its",
        "HOST": "",
        "PORT": ""}}

VIRTUALENV = 'src-its'


SITE_TITLE = 'SRC-ITS Django'
SITE_TAGLINE = None
POSTGIS_VERSION = (2, 1, 2)
