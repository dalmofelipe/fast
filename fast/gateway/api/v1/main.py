from fastapi import APIRouter

from fast.gateway.api.v1.endpoints import index
from fast.gateway.api.v1.endpoints import user

api_v1_routes = APIRouter(prefix='/api/v1', tags=['APIv1'])

api_v1_routes.include_router(index.routes)
api_v1_routes.include_router(user.routes, prefix='/users')
