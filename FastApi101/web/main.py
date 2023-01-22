from fastapi import FastAPI

from FastApi101.api.v1 import index as index_apiv1
from FastApi101.api.v1 import users as users_apiv1

from FastApi101.api.v2 import dashboard as dashboard_apiv2
from FastApi101.api.v2 import users as users_apiv2


webapp = FastAPI(help="WebAPP com FastApi101")


webapp.include_router(index_apiv1.routes)
webapp.include_router(users_apiv1.routes)

webapp.include_router(dashboard_apiv2.routes)
webapp.include_router(users_apiv2.routes)


@webapp.get('/')
def root_index():
    return {
        "msg": "Hello World!",
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    }
