from typing import Any

from fastapi import APIRouter, HTTPException, Query, status

from fast.models.user import User
from fast.gateway.api.v1.serializers.user import UserCreate, UserUpdate, UserOutput
from fast.repositories.users import UserRepository

routes = APIRouter()
user_repository = UserRepository()

PAGE_DEFAULT = 1
LIMIT_DEFAULT = 5


@routes.get(
    '/'
)
def route_list_all(
    page: int = Query(default=PAGE_DEFAULT),
    limit: int = Query(default=LIMIT_DEFAULT),
    name: str = Query(default=''),
    email: str = Query(default=''),
):
    global user_repository
    if page < 1 or limit < 1:
        return None
    offset = (page * limit) - limit

    return user_repository.get_all(offset, limit, name, email)


@routes.get(
    '/{id:int}'
)
def route_get_one(
    id: int
):
    global user_repository
    return user_repository.find_by_id(id)


@routes.get(
    '/find',
    status_code=status.HTTP_200_OK
)
def route_find_by_email(
    email: str = Query(default=''),
):
    global user_repository
    return user_repository.find_by_email(email)


@routes.post(
    '/', 
    status_code=status.HTTP_201_CREATED,
    response_model=UserOutput
)
def route_save(
    user_input: UserCreate
)   -> Any:
    global user_repository
    name, email, password = user_input.get_properties()
    
    is_valid, errors = User.validate(name, email, password)
    user_db = user_repository.find_by_email(email)

    if user_db or not is_valid:
        errors['email'] = 'E-mail já esta em uso no sistema'
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                'refs': 'api.v1.endpoints.user:route_save',
                'msg': 'Não foi possível salvar usuário via API',
                'errors': errors,
            },
        )

    if is_valid and len(errors) == 0 and not user_db:
        return user_repository.save(name, email, password)


@routes.put(
    '/{id:int}', 
    status_code=status.HTTP_200_OK,
    response_model=UserOutput
)
def route_update(
    id: int,
    user_data: UserUpdate
)   -> Any:
    global user_repository
    _, name, email, password = user_data.get_properties()
    return user_repository.update(id, name, email, password)


@routes.delete(
    '/{id:int}',
    status_code=status.HTTP_200_OK
)
def route_delete(
    id: int
):
    global user_repository
    return user_repository.delete(id)
