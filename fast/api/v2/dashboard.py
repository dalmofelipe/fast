from fastapi import APIRouter


routes = APIRouter(prefix='/api/v2/dashboard', tags=['APIv2'])


@routes.get('/')
def root_dashboard():
    return {
        'users': {'ativos': 2, 'admins': 1, 'desativados': 0},
        'levels': ['admin', 'moderador', 'normal'],
        'docs': 'http://localhost:8000/docs',
        'redoc': 'http://localhost:8000/redoc',
    }
