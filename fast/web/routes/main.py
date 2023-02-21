from fastapi import APIRouter

from fast.web.routes.root import root_routes
from fast.web.routes.auth import auth_routes


web_routes = APIRouter()
web_routes.include_router(router=root_routes)
web_routes.include_router(router=auth_routes)
