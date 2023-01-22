from fastapi import APIRouter


routes = APIRouter(
    prefix='/api/v1',
    tags=['APIv1']
)


@routes.get('/')
def root_index():
    return {
        "msg": "Hello World!",
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    }
