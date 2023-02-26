from fastapi import Request, Form, status
from fastapi.responses import RedirectResponse

from fast.core import validations, bcrypt
from fast.infra.database import get_session
from fast.models.user import User
from fast.repositories.users import UserRepository
from fast.web import main

repository = UserRepository(get_session)


def register_view(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'Crie Sua Conta'
    context['errors'] = {}
    context['user'] = {}
    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def register_handle(
    request: Request, name: str | None = '', email: str | None = '', 
    password: str | None = '', confirm_pass: str | None = ''
):
    global repository

    context = {}
    context['request'] = request
    context['errors'] = {}
    context['user'] = {}

    if request.method == 'POST':
        context['user'] = {
            'name': name,
            'email': email,
            'password': '',
            'confirm_pass': '',
        }
        is_valid, errors = validations.user_data(
            name, email, password, confirm_pass
        )
        context['errors'] = errors
        user = repository.find_by_email(email)

        if isinstance(user, User) and user.email == email:
            context['errors']['email'] = f'O email "{email}" já esta em uso'
        elif is_valid:
            repository.save(name, email, password)
            context['user'] = {}
            context['created'] = 'Usuário registrado com sucesso!'

    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def login_handle(
    request: Request, email: str | None = '', password: str | None = ''
):
    global repository

    context = {}
    context['request'] = request
    context['title'] = 'Entrar'
    context['user'] = {}

    if request.method == 'POST':
        user = repository.find_by_email(email)
        if user and bcrypt.check_password(
            hash_password = user.password, password_text = password
        ):
            return RedirectResponse(
                main.webapp.url_path_for(name='index'), 
                status_code=status.HTTP_303_SEE_OTHER
            )

    return main.templates.TemplateResponse(
        'pages/auth/login.html', context=context
    )
