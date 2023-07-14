from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast.api.v1.main import api_v1_routes
from fast.api.v2 import dashboard as dashboard_apiv2
from fast.api.v2 import users as users_apiv2
from fast.infra.config import settings

env = settings['ENVIRONMENT']
print(f'INFO:     {env} Env')

from fast.web.routes.main import web_routes


# Handlers
async def not_found_error(
    request: Request, 
    exc: HTTPException
):
    return templates.TemplateResponse(
        'pages/404.html', { 'request': request }, status_code=404
    )

async def internal_error(
    request: Request, 
    exc: HTTPException
):
    return templates.TemplateResponse(
        'pages/500.html', { 'request': request }, status_code=500
    )


exception_handlers = {
    404: not_found_error,
    500: internal_error
}

webapp = FastAPI(
    help='WebAPP com FastApi101',
    exception_handlers=exception_handlers
)

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
