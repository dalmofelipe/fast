from fastapi import Request

from fast.core import bcrypt, validations
from fast.infra.database import get_session
from fast.domain.models.user import User
from fast.domain.repositories.users import UserRepository
from fast.presentation.web import main

user_repo = UserRepository(get_session)


def register_handle(
    request: Request, 
    name: str | None = '', 
    email: str | None = '', 
    password: str | None = '', 
    confirm_pass: str | None = ''
):
    global user_repo

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
        is_valid, errors = validations.check_input_user(
            name, email, password, confirm_pass
        )
        context['errors'] = errors
        user = user_repo.find_by_email(email)

        if isinstance(user, User) and user.email == email:
            context['errors']['email'] = f'E-mail já esta em uso'
        elif is_valid:
            user_repo.save(name, email, password)
            context['user'] = {}
            context['created'] = 'Usuário registrado com sucesso!'
        if len(context['errors']) == 0:
            return main.templates.TemplateResponse(
                'pages/auth/login.html', context=context
            )
    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def login_handle(
    request: Request, 
    email: str | None = '', 
    password: str | None = ''
):
    global user_repo

    context = {}
    context['request'] = request
    context['title'] = 'Entrar'
    context['user'] = {}

    if request.method == 'POST':
        user = user_repo.find_by_email(email)
        if user and bcrypt.check_password(
            password_text = password, 
            hash_password = user.password 
        ):
            context['user'] = user
            # return RedirectResponse(
            #     main.webapp.url_path_for(name='index'), 
            #     status_code=status.HTTP_303_SEE_OTHER,
            # )
            return main.templates.TemplateResponse(
                'pages/index.html', context=context
            )

    return main.templates.TemplateResponse(
        'pages/auth/login.html', context=context
    )
