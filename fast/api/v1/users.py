from fastapi import APIRouter, Query

from fast.repositories import user as repo_user
from fast.core.validations import check_email


routes = APIRouter(
    prefix='/api/v1/users',
    tags=['APIv1']
)


@routes.get('/')
def get_all(
    page: int = Query(),
    limit: int = Query()
):
    """
    """
    if page < 1 or limit < 5:
        return None
    offset = page * limit
    users = repo_user.get_all(offset, limit)
    return users


@routes.get('/find')
def find_by_email(
    email:str = Query()
):
    """
    """
    if check_email(email):
        user = repo_user.find_by_email(email)
        return user
    return None
