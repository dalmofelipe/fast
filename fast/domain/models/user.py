from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):

    __tablename__ = 'tb_users'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=20)
    email: str = Field(unique=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.now)

    @classmethod
    def is_valid():
        ...
