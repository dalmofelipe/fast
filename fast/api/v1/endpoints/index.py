from fastapi import APIRouter

routes = APIRouter()


@routes.get('/')
def route_index():
    return {
        'msg': 'Hello World!',
        'docs': 'http://localhost:8000/docs',
        'redoc': 'http://localhost:8000/redoc',
    }
