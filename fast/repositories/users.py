from sqlmodel import select, text
from sqlalchemy.exc import NoResultFound

from fast.core.bcrypt import hash_password
from fast.models.user import IUserRepository, User
from fast.repositories.base import Base


class UserRepository(Base, IUserRepository):

    def __init__(self) -> None:
        Base.__init__(self)


    def save(
        self, name: str, email: str, password: str
    ) -> User:
        """ """
        user = User()
        user.name = name
        user.email = email
        user.password = hash_password(password)

        with self.get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        
        return user


    def get_all(self, offset: int, limit: int, name: str, email: str):
        """ """
        with self.get_session() as session:
            query = (
                select(
                    User.id,
                    User.name,
                    User.email
                )
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
            return session.exec(statement).first() or None


    def find_by_name(self, name: str):
        """ """
        with self.get_session() as session:
            statement = select(
                User.id, 
                User.name,
                User.email
            ).where(User.name == name)
            user = session.exec(statement).first()
            return user


    def find_by_id(self, id: str):
        """ """
        with self.get_session() as session:
            statement = select(
                User.id, 
                User.name,
                User.email
            ).where(User.id == id)
            user = session.exec(statement).first()
            return user


    def update(self, id: int, name: str = None, email: str = None, password: str = None):
        """ """
        user : User = None

        with self.get_session() as session:
            statement = select(User).where(User.id == id)

            try: 
                results = session.exec(statement)
                user = results.one()
            except NoResultFound:
                return None

        user.name = name or user.name
        user.email = email or user.email

        if password != None:
            user.password = hash_password(password)

        with self.get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        
        return user
    
    
    def delete(self, id: int):
        """ """
        user : User = None

        with self.get_session() as session:
            statement = select(User).where(User.id == id)

            try: 
                results = session.exec(statement)
                user = results.one()
            except NoResultFound:
                return 0

            session.delete(user)
            session.commit()
        
        return user.id
