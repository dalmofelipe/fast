from sqlmodel import select, text

from fast.database.config import get_sqlite_session
from fast.models.user import User


def save(name: str, email: str, password: str):
    """ """
    user = User()
    user.name = name
    user.email = email
    user.password = password

    with get_sqlite_session() as session:
        session.add(user)
        session.commit()


def get_all(offset: int, limit: int, name: str, email: str):
    """ """
    with get_sqlite_session() as session:
        query = (
            select(User)
            .offset(offset)
            .limit(limit)
            .where(text(f"name like '%{name}%'"))
            .where(text(f"email like '%{email}%'"))
        )
        users = session.exec(query).fetchall()
    return users


def find_by_email(email: str):
    """ """
    with get_sqlite_session() as session:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user


def find_by_name(name: str):
    """ """
    with get_sqlite_session() as session:
        statement = select(User).where(User.name == name)
        user = session.exec(statement).first()
        return user


def find_by_id(id: str):
    """ """
    with get_sqlite_session() as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()
        return user
