from decouple import config


class Settings:

    ENVIRONMENT = config('ENVIRONMENT', cast=str, default='development')
    DB_STRING_CONN = config('DB_STRING_CONN', cast=str, default="sqlite:///database.sqlite")
    PORT = config('PORT', cast=int, default=8000)
