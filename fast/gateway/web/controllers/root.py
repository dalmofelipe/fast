from fastapi import Request
from fastapi.responses import RedirectResponse

from fast.gateway.web import main


context = {
    'request': None,
    'endpoint': '',
    'errors': {},
    'user': {}
}


def index_login():
    return RedirectResponse(main.webapp.url_path_for(name='login'))


def index(request: Request):
    context['request'] = request
    return main.templates\
        .TemplateResponse('pages/index.html', context=context)


def contato(request: Request):
    context['request'] = request
    context['describe'] = \
        '[ Context Backend ] Essa view demonstra integração HTML, CSS e JavaScript'
    return main.templates\
        .TemplateResponse('pages/contato.html', context=context)
