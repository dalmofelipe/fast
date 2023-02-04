from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from pyweb.web import main

routes = APIRouter(
    prefix="/auth"
)


@routes.get(
    "/register", 
    name='register',
    response_class=HTMLResponse, 
    include_in_schema=False
)
def register_view(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'Crie Sua Conta'
    return main.templates.TemplateResponse('pages/auth/register.html', context=context)


@routes.post(
    '/register',
    response_class=HTMLResponse, 
    include_in_schema=False
)
def register_handle_post(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirmpass: str = Form(...),
):
    context = {}
    context['request'] = request

    if request.method == 'POST':
        print(f"register data -> {name} | {email} | {password} | {confirmpass} ")

    return main.templates.TemplateResponse('pages/auth/register.html', context=context)


@routes.get(
    "/login", 
    name='login', 
    response_class=HTMLResponse, 
    include_in_schema=False
)
def login(
    request: Request
):
    context = {}
    context['request'] = request
    context['title'] = 'Entrar'
    return main.templates.TemplateResponse('pages/auth/login.html', context=context)


@routes.post(
    "/login", 
    response_class=HTMLResponse, 
    include_in_schema=False
)
def login_handle_post(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    context = {}
    context['request'] = request
    context['title'] = 'Entrar'

    if request.method == 'POST':
        print(f"login data: {email} | {password}")
    
    return main.templates.TemplateResponse('pages/auth/login.html', context=context)
