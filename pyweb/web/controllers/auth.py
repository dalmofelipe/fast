from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from pyweb.web import main
from pyweb.models.user import User
from pyweb.repositories import user as user_repository
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
    context['user_data'] = {}
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
    confirm_pass: str = Form(...)
):
    context = {}
    context['request'] = request
    context['errors'] = {}
    context['user_data'] = {}

    if request.method == 'POST':
        context['user_data'] = {
            "name": name, 
            "email": email, 
            "password": '', 
            "confirm_pass": ''
        }
        is_valid, errors = user_input_form_data_is_valid(name, email, password, confirm_pass)
        context['errors'] = errors
        user = user_repository.find_by_email(email)

        if isinstance(user, User) and user.email == email:
            context['errors']['email_error'] = f'O email "{email}" já esta em uso'
        elif is_valid: 
            user_repository.save(name, email, password)
            context['user_data'] = {}
            context['created'] = "Usuário registrado com sucesso!"

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
