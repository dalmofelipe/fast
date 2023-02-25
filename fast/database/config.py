from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from fast.models import user

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


def get_sqlite_session():
    sqlite_engine = create_engine('sqlite:///fast/database/database.sqlite', echo=False)
    user.SQLModel.metadata.create_all(sqlite_engine)
    return Session(sqlite_engine)


def get_mysql_session():
    stringconn = 'mysql+pymysql://dev:123456@localhost:3306/fast?charset=utf8'
    mysql_engine = create_engine(stringconn, echo=True)
    user.SQLModel.metadata.create_all(mysql_engine)
    return Session(mysql_engine)
