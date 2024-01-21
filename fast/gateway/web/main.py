from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast.gateway.api.v1.main import api_v1_routes
from fast.gateway.web.handlers import exception_handlers
from fast.gateway.web.routes.main import web_routes
from fast.infra.config import settings

print(f'INFO:     {settings["ENVIRONMENT"].upper()} Environment')


webapp = FastAPI(
    help='WebAPP com FastApi101',
    exception_handlers=exception_handlers
)

webapp.mount(
    '/fast/gateway/web/statics',
    StaticFiles(directory='fast/gateway/web/statics'),
    name='statics',
)

templates = Jinja2Templates(directory='fast/gateway/web/templates')


# Rotas das APIs
webapp.include_router(api_v1_routes)

# Routas da Webapp
webapp.include_router(web_routes)
