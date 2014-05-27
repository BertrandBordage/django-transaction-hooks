import os

from .settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
        'NAME': 'dtc',
        },
    }


if 'DTC_PG_USERNAME' in os.environ:
    DATABASES['default'].update(
        {
            'USER': os.environ['DTC_PG_USERNAME'],
            'PASSWORD': '',
            'HOST': 'localhost',
            }
        )
