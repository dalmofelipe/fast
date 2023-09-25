from fastapi import APIRouter, Query, status, HTTPException

from fast.gateway.api.v1.serializers.user import UserInput

from fast.core import validations
from fast.infra.database import get_session
from fast.adapters.repositories.users import UserRepository


routes = APIRouter()
repository = UserRepository(get_session)

PAGE_DEFAULT = 1
LIMIT_DEFAULT = 5


@routes.get('/')
def route_list_all(
    page: int = Query(default=PAGE_DEFAULT),
    limit: int = Query(default=LIMIT_DEFAULT),
    name: str = Query(default=''),
    email: str = Query(default=''),
):
    global repository
    if page < 1 or limit < 1:
        return None
    offset = (page * limit) - limit

    return repository.get_all(offset, limit, name, email)


@routes.post('/', status_code=status.HTTP_201_CREATED)
def route_save(user_input: UserInput):
    global repository
    name, email, password, confirm_pass = user_input.get_properties()
    
    is_valid, errors = validations.check_input_user(
        name, email, password, confirm_pass
    )
    user_db = repository.find_by_email(email)

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
        repository.save(name, email, password)


@routes.get('/find')
def route_find_by_email(email: str = Query(default='')):
    global repository
    return repository.find_by_email(email)
