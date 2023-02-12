from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse

from fast.web import main

routes = APIRouter(
    prefix=""
)


@routes.get('/', include_in_schema=False)
def root_index_login():
    return RedirectResponse(main.webapp.url_path_for(name='login'))


@routes.get('/index', include_in_schema=False, response_class=HTMLResponse)
def root_index(request:Request):
    context = {}
    context['request'] = request
    context['title'] = 'INDEX'
    context['name'] = 'Dalmo Felipe'
    context['github'] = 'github.com/dalmofelipe'
    context['describe'] = 'Demonstra integração CSS, JS, HTML'
    return main.templates.TemplateResponse('pages/index.html', context=context)
