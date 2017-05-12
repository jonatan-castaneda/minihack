from .base import *
import os

SECRET_KEY = 'bd&hdp6^bq16&j2gkmer426lx3*uu_og9+1o8&pczp03$in6g_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'minihack',
        'USER': 'user_minihack',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}