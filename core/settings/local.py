from .includes.common import *

DEBUG = True

# Make these unique, and don't share it with anybody.
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
<<<<<<< HEAD
        "NAME": "cccs",
        "USER": "cccs",
        "PASSWORD": DBPASSWORD,
        "HOST": "",
        "PORT": ""}}

VIRTUALENV = 'cccs'


SITE_TITLE = 'Cross-Cultural Consulting Services'
=======
        "NAME": "its",
        "USER": "its",
        "PASSWORD": "src-its",
        "HOST": "",
        "PORT": ""}}

VIRTUALENV = 'src-its'


SITE_TITLE = 'SRC-ITS Django'
>>>>>>> e360d8da8c4266ff09c239cd6466e4c64e7be2d9
SITE_TAGLINE = None
POSTGIS_VERSION = (2, 1, 2)
