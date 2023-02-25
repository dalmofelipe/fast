from fastapi import Request, Form

from fast.web import main
from fast.models.user import User
from fast.core.password import hash_password
from fast.repositories import user as user_repository
from fast.core import validations


def register_view(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'Crie Sua Conta'
    context['errors'] = {}
    context['user_data'] = {}
    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def register_handle(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_pass: str = Form(...),
):
    context = {}
    context['request'] = request
    context['errors'] = {}
    context['user_data'] = {}

    if request.method == 'POST':
        context['user_data'] = {
            'name': name,
            'email': email,
            'password': '',
            'confirm_pass': '',
        }
        is_valid, errors = validations.user_data(
            name, email, password, confirm_pass
        )
        context['errors'] = errors
        user = user_repository.find_by_email(email)

        if isinstance(user, User) and user.email == email:
            context['errors'][
                'email_error'
            ] = f'O email "{email}" já esta em uso'
        elif is_valid:
            user_repository.save(name, email, hash_password(password))
            context['user_data'] = {}
            context['created'] = 'Usuário registrado com sucesso!'

    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def login_view(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'Entrar'
    return main.templates.TemplateResponse(
        'pages/auth/login.html', context=context
    )


def login_handle(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    context = {}
    context['request'] = request
    context['title'] = 'Entrar'

    if request.method == 'POST':
        print(f'login data: {email} | {password}')

    return main.templates.TemplateResponse(
        'pages/auth/login.html', context=context
    )
