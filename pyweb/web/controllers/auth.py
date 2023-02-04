from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from pyweb.web import main
from pyweb.core.user import save_user_on_db
from pyweb.core.validations import user_input_form_data_is_valid


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
    context['errors'] = {}
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
    confirm: str = Form(...)
):
    context = {}
    context['request'] = request
    context['errors'] = {}

    if request.method == 'POST':
        is_valid, errors = user_input_form_data_is_valid(name, email, password, confirm)
        if is_valid:  
            save_user_on_db(name, email, password)
            context['created'] = "Usuário registrado com sucesso!"
        else:
            context['errors'] = errors

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
