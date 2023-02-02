from fastapi import APIRouter


routes = APIRouter(
    prefix='/api/v2/users',
    tags=['APIv2']
)


@routes.get('/')
def root_users():
    return {
        "users": [
            {
                "name": "Dalmo",
                "email": "dalmo@email.com",
                "level_id": 0
            },
            {
                "name": "Felipe",
                "email": "felipe@email.com",
                "level_id": 3
            },
        ],
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    }
