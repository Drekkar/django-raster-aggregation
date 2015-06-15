"""
Settings for django-raster-aggregation tests.
"""
import os

SECRET_KEY = 'testkey'

INSTALLED_APPS = (
    'raster',
    'raster_aggregation',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': os.environ.get('DB_USER', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}

DEBUG = True

ROOT_URLCONF = 'raster_aggregation.urls'
