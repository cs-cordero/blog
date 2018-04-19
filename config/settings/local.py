from .common import *

import os

BASE_DIR = os.path.abspath(os.path.join(__file__, '..', '..', '..'))

DEBUG = True
SECRET_KEY = 'x1&6njoiwqnje!y63((#$y!o(y)@929&%!y31dftl0_ef(xrnz'
ALLOWED_HOSTS = [
    '*'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cs-cordero',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
