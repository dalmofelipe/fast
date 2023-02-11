from sqlmodel import select

from pyweb.database.config import get_session
from pyweb.models.user import User


def save(
    name:str, 
    email:str, 
    password:str
):
    """
    """
    user = User()
    user.name = name 
    user.email = email
    user.password = password # bcryptar essa senha!
    
    with get_session() as session:
        session.add(user)
        session.commit()


def get_all(
    offset: int,
    limit: int
):
    """
    """
    with get_session() as session:
        query = select(User).offset(offset).limit(limit)
        users = session.exec(query).all()
    return users


def find_by_email(
    email:str
):
    """
    """
    with get_session() as session:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user
