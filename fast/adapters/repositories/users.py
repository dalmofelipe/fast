from sqlmodel import select, text

from fast.adapters.repositories.base import Base
from fast.core.bcrypt import hash_password
from fast.domain.models.user import User, IUserRepository


class UserRepository(Base, IUserRepository):

    def __init__(self, session) -> None:
        Base.__init__(self, session)

    def save(self, name: str, email: str, password: str):
        """ """
        user = User()
        user.name = name
        user.email = email
        user.password = hash_password(password)

        with self.get_session() as session:
            session.add(user)
            session.commit()

    def get_all(self, offset: int, limit: int, name: str, email: str):
        """ """
        with self.get_session() as session:
            query = (
                select(User)
                .offset(offset)
                .limit(limit)
                .where(text(f"name like '%{name}%'"))
                .where(text(f"email like '%{email}%'"))
            )
            users = session.exec(query).fetchall()
        return users

    def find_by_email(self, email: str):
        """ """
        with self.get_session() as session:
            statement = select(User).where(User.email == email)
            user = session.exec(statement).first()
            return user

    def find_by_name(self, name: str):
        """ """
        with self.get_session() as session:
            statement = select(User).where(User.name == name)
            user = session.exec(statement).first()
            return user

    def find_by_id(self, id: str):
        """ """
        with self.get_session() as session:
            statement = select(User).where(User.id == id)
            user = session.exec(statement).first()
            return user
