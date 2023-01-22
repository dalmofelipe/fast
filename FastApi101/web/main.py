from fastapi import FastAPI


webapp = FastAPI(help="WebAPP com FastApi101")


@webapp.get('/')
def root_index():
    return {
        "msg": "Hello World!",
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc",
    }
