from decouple import config

ENV =  config('ENVIRONMENT', cast=str, default='dev')

settings = {}

if ENV == 'production':
    settings = {
        'DB_PROD': config('DB_PROD'),
        'DB_HOST': config('DB_HOST'),
        'DB_PORT': config('DB_PORT'),
        'DB_NAME': config('DB_NAME'),
        'DB_USER': config('DB_USER'),
        'DB_PASS': config('DB_PASS'),
    }
else:
    settings = {
        'DB_DEV': config('DB_DEV', default="sqlite:///database.sqlite"),
    }

settings['ENVIRONMENT'] = ENV
