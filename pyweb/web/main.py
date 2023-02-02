from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pyweb.api.v1 import index as index_apiv1
from pyweb.api.v1 import users as users_apiv1

from pyweb.api.v2 import dashboard as dashboard_apiv2
from pyweb.api.v2 import users as users_apiv2


webapp = FastAPI(help="WebAPP com FastApi101")
webapp.mount('/pyweb/web/statics', StaticFiles(directory='pyweb/web/statics'), name='statics')
templates = Jinja2Templates(directory='pyweb/web/templates')


webapp.include_router(index_apiv1.routes)
webapp.include_router(users_apiv1.routes)

webapp.include_router(dashboard_apiv2.routes)
webapp.include_router(users_apiv2.routes)


@webapp.get('/', include_in_schema=False)
def root_index(request: Request):
    context = {}
    context['request'] = request
    context['name'] = 'Dalmo'
    context['github'] = 'github.com/dalmofelipe'
    return templates.TemplateResponse('pages/index.html', context=context)
