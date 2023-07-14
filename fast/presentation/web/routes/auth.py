from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from fast.presentation.web.controllers import auth as auth_controller

auth_routes = APIRouter(prefix='/auth')


@auth_routes.get(
    '/register', name='register', response_class=HTMLResponse, 
    include_in_schema=False
)
@auth_routes.post(
    '/register', response_class=HTMLResponse, include_in_schema=False
)
def route_register_handle(
    request: Request,
    name: str | None = Form(default=''),
    email: str | None = Form(default=''),
    password: str | None = Form(default=''),
    confirm_pass: str | None = Form(default=''),
):
    return auth_controller.register_handle(
        request, name, email, password, confirm_pass
    )


@auth_routes.get(
    '/login', name='login', include_in_schema=False
)
@auth_routes.post(
    '/login', response_class=HTMLResponse, include_in_schema=False
)
def route_login_handle(
    request: Request,
    email: str | None = Form(default=''),
    password: str | None = Form(default=''),
):
    return auth_controller.login_handle(request, email, password)
