from typing import Optional

from fastapi import APIRouter, Query

from fast.api.v1.controllers import user as user_controller


user_routes = APIRouter(prefix='/users')


@user_routes.get('/')
def get_all(
    page: Optional[int] = Query(default=user_controller.PAGE_DEFAULT),
    limit: Optional[int] = Query(default=user_controller.LIMIT_DEFAULT),
    name: Optional[str] = Query(default=''),
    email: Optional[str] = Query(default=''),
):
    return user_controller.get_all(page, limit, name, email)


@user_routes.get('/find')
def find_by_email(email: Optional[str] = Query(default='')):
    return user_controller.find_by_email(email)
