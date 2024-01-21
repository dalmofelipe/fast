from fastapi import APIRouter

from fast.config.environment import settings

PORT = settings['PORT']

routes = APIRouter()


@routes.get('/')
def route_index():
    return {
        'msg': 'Hello World!',
        'docs': f'http://localhost:{PORT}/docs',
        'redoc': f'http://localhost:{PORT}/redoc',
    }
