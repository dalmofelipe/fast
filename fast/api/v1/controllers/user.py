from fast.repositories import user as user_repository

PAGE_DEFAULT = 1
LIMIT_DEFAULT = 5


def get_all(
    page:int, limit:int , name:str, email:str
):
    """
    """
    if page < 1 or limit < 1:
        return None
    offset = (page * limit) - limit
    users = user_repository.get_all(offset, limit, name, email)
    return users


def find_by_email(
    email:str
):
    """
    """
    return user_repository.find_by_email(email)
