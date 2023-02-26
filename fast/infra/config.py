from decouple import config


settings = {
    'ENVIRONMENT': config('ENVIRONMENT', cast=str, default='DEV'),
    'DB_DEV': config('DB_DEV'),
    'DB_PROD': config('DB_PROD'),
    'DB_HOST': config('DB_HOST'),
    'DB_PORT': config('DB_PORT'),
    'DB_NAME': config('DB_NAME'),
    'DB_USER': config('DB_USER'),
    'DB_PASS': config('DB_PASS'),
}
