from fastapi import APIRouter

from fast.api.v1.routes.index import index_routes
from fast.api.v1.routes.user import user_routes


api_v1_routes = APIRouter(prefix='/api/v1', tags=['APIv1'])


api_v1_routes.include_router(index_routes)
api_v1_routes.include_router(user_routes)
