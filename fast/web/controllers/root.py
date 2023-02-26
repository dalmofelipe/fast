from fastapi import Request
from fastapi.responses import RedirectResponse

from fast.web import main


def index_login():
    return RedirectResponse(main.webapp.url_path_for(name='login'))


def index(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'INDEX'
    context['name'] = 'Dalmo Felipe'
    context['github'] = 'github.com/dalmofelipe'
    context['describe'] = \
        'Essa view demonstra integração HTML, CSS e JavaScript'
    return main.templates.TemplateResponse('pages/index.html', context=context)
