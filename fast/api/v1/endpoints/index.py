from fastapi import APIRouter, Cookie

from fast.config.environment import Settings

PORT = Settings.PORT

routes = APIRouter()


@routes.get('/')
async def route_index(user : str | None = Cookie(None)):
    return {
        'msg': 'Hello World!',
        'user-coookie': user, 
        'docs': f'http://localhost:{PORT}/docs',
        'redoc': f'http://localhost:{PORT}/redoc',
    }
