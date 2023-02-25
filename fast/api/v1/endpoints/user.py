from fastapi import APIRouter, Query, status, HTTPException

from fast.api.v1.serializers.user import UserInput

from fast.core.password import hash_password
from fast.core import validations
from fast.database.config import get_mysql_session
from fast.repositories.users import UserRepository


routes = APIRouter()
repository = UserRepository(get_mysql_session)

PAGE_DEFAULT = 1
LIMIT_DEFAULT = 5



@routes.get('/')
def route_list_all(
    page: int = Query(default = PAGE_DEFAULT),
    limit: int = Query(default = LIMIT_DEFAULT),
    name: str = Query(default = ''),
    email: str = Query(default = ''),
):
    global repository
    if page < 1 or limit < 1:
        return None
    offset = (page * limit) - limit
    
    return repository.get_all(offset, limit, name, email)



@routes.post('/', status_code = status.HTTP_201_CREATED)
def route_save(user_input: UserInput):
    global repository
    name = user_input.name
    email = user_input.email
    password = user_input.password
    confirm_pass = user_input.confirm_pass

    is_valid, errors = validations.user_data(name, email, password, confirm_pass)
    user_db = repository.find_by_email(email)

    if user_db or not is_valid: 
        errors['email'] = 'este email já esta em uso no sistema'
        raise HTTPException(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail = {
                "refs": "api.v1.routes.user:route_save",
                "msg": "não foi possível salva usuário via api",
                "errors": errors
            }
        )

    if is_valid and len(errors) == 0:
        repository.save(name, email, hash_password(password))



@routes.get('/find')
def route_find_by_email(email: str = Query(default='')):
    global repository
    return repository.find_by_email(email)
