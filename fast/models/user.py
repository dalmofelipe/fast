from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from fast.core.validations import check_email


class IUserRepository(ABC):

    @abstractmethod 
    def save(self, name: str, email: str, password: str): pass

    @abstractmethod 
    def get_all(self, offset: int, limit: int, name: str, email: str): pass

    @abstractmethod 
    def find_by_email(self, email: str): pass

    @abstractmethod 
    def find_by_name(self, name: str): pass

    @abstractmethod 
    def find_by_id(self, id: str): pass

    @abstractmethod
    def update(self, id:int, name: str = None, email: str = None, password: str = None): pass

    @abstractmethod
    def delete(self, id:int): pass


class User(SQLModel, table=True):

    __tablename__ = 'tb_users'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=20)
    email: str = Field(unique=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.now)

    def validate(name, email, password):
        errors = {}

        if len(name) < 3 or len(name) > 20:
            errors['name'] = 'O nome de conter entre 3 e 20 caracteres'

        if not check_email(email):
            errors['email'] = f'E-mail é inválido'

        if len(password) < 6 or len(password) > 12:
            errors['password'] = 'A senha deve ter entre 6 e 12 caracteres'

        if len(errors) > 0: return False, errors

        return True, {}
