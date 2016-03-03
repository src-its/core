from .includes.common import *

DEBUG = True

# Make these unique, and don't share it with anybody.
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
	"NAME": "caweb",
	"USER": "caweb",
        "PASSWORD": DBPASSWORD,
        #"HOST": "",
	"HOST": "127.0.0.1",
        "PORT": "5432"}}

VIRTUALENV = 'ca-web'


SITE_TITLE = 'Cross-Cultural Consulting Services'
SITE_TAGLINE = None
