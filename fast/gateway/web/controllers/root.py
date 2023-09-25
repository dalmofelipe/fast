from fastapi import Request
from fastapi.responses import RedirectResponse

from fast.gateway.web import main


def index_login():
    return RedirectResponse(main.webapp.url_path_for(name='login'))


def index(request: Request):
    context = {}
    context['request'] = request
    context['describe'] = \
        '[ Backend ] Essa view demonstra integração HTML, CSS e JavaScript'
    return main.templates\
        .TemplateResponse('pages/index.html', context=context)
