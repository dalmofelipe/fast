import json

from fastapi import Request, status
from fastapi.responses import RedirectResponse

from fast.web import main


context = {
    'request': None,
    'endpoint': '',
    'errors': {},
    'user': {}
}


def index(request: Request):
    context['request'] = request
    user_cookie = request.cookies.get('user')
    if user_cookie:
        context['user'] = json.loads(user_cookie)
    else: 
        return RedirectResponse(
            main.webapp.url_path_for(name='login'), 
            status_code=status.HTTP_303_SEE_OTHER,
        )

    return main.templates\
        .TemplateResponse('pages/index.html', context=context)


def contato(request: Request):
    context['request'] = request
    user_cookie = request.cookies.get('user')
    
    if user_cookie:
        context['user'] = json.loads(user_cookie)
    else: 
        return RedirectResponse(
            main.webapp.url_path_for(name='login'), 
            status_code=status.HTTP_303_SEE_OTHER,
        )

    context['describe'] = \
        '[ Context Backend ] Essa view demonstra integração HTML, CSS e JavaScript'
    return main.templates\
        .TemplateResponse('pages/contato.html', context=context)
