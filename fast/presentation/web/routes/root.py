from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fast.presentation.web.controllers import root as root_controller

root_routes = APIRouter(prefix='')


@root_routes.get(
    '/', name='index', include_in_schema=False, 
    response_class=HTMLResponse
)
def route_index(request: Request):
    return root_controller.index(request)
