from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast.api.v1.routes.main import api_v1_routes

from fast.api.v2 import dashboard as dashboard_apiv2
from fast.api.v2 import users as users_apiv2

from fast.web.routes.main import web_routes


webapp = FastAPI(help='WebAPP com FastApi101')
webapp.mount(
    '/fast/web/statics',
    StaticFiles(directory='fast/web/statics'),
    name='statics',
)
templates = Jinja2Templates(directory='fast/web/templates')


# Rotas das APIs
webapp.include_router(api_v1_routes)

webapp.include_router(dashboard_apiv2.routes)
webapp.include_router(users_apiv2.routes)


# Routas da Webapp
webapp.include_router(web_routes)
