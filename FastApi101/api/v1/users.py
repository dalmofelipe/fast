from fastapi import APIRouter


routes = APIRouter(
    prefix='/api/v1/users',
    tags=['APIv1']
)


@routes.get('/')
def root_users():
    return {
        "users": [
            {
                "name": "Dalmo",
                "email": "dalmo@email.com",
                "level": "admin"
            },
            {
                "name": "Felipe",
                "email": "felipe@email.com",
                "level": "normal"
            },
        ],
        "count": 2,
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    }
