from fastapi import APIRouter

from fast.api.v1.controllers import index as index_controller


index_routes = APIRouter()


@index_routes.get('/')
def root_index():
    return index_controller.home()
