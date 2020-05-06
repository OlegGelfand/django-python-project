import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pythondb',
        'USER': 'oleggelfand',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
DEBUG = True