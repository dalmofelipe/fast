from fastapi import Request

from fast.core import bcrypt, validations
from fast.models.user import User
from fast.web import main
from fast.repositories.users import UserRepository

user_repository = UserRepository()
context = {
    'request': None,
    'endpoint': '',
    'errors': {},
    'user': {}
}

def register_handle(
    request: Request, 
    name: str | None = '',  
    email: str | None = '', 
    password: str | None = '', 
    confirm_pass: str | None = ''
):
    global user_repository, context
    context['request'] = request
    context['endpoint'] = str(request.url).split('/')[-1]
    
    if request.method == 'POST':
        context['user'] = { 'name': name, 'email': email }
        is_valid, errors = validations\
            .check_input_user(name, email, password, confirm_pass)
        context['errors'] = errors
        user_from_db = user_repository.find_by_email(email)

        if isinstance(user_from_db, User) and user_from_db.email == email:
            context['errors']['email'] = f'E-mail já esta em uso'
        elif is_valid:
            user_repository.save(name, email, password)
            context['user'] = {}
            context['created'] = 'Usuário registrado com sucesso!'

        if len(context['errors']) == 0:
            return main.templates\
                .TemplateResponse('pages/auth/login.html', context=context)

    return main.templates\
        .TemplateResponse('pages/auth/register.html', context=context)


def login_handle(
    request: Request, 
    email: str | None = '', 
    password: str | None = ''
):
    global user_repository, context
    context['request'] = request
    context['endpoint'] = str(request.url).split('/')[-1]

    if request.method == 'POST':
        user_from_db = user_repository.find_by_email(email)
        
        if user_from_db and bcrypt\
            .check_password(password, user_from_db.password):

            context['user'] = {
                'name': user_from_db.name,
                'email': user_from_db.email
            }
            headers = { 'Location': '/' }
            return main.templates\
                .TemplateResponse('pages/index.html', context=context, headers=headers, 
                    status_code=200)
            
            # return RedirectResponse(
            #     main.webapp.url_path_for(name='index'), 
            #     status_code=status.HTTP_303_SEE_OTHER
            # )

    return main.templates\
        .TemplateResponse('pages/auth/login.html', context=context)
