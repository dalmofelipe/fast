from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from fast.models import user

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

sqlite_engine = create_engine('sqlite:///fast/database/database.sqlite', echo=False)
user.SQLModel.metadata.create_all(sqlite_engine)


def get_sqlite_session():
    return Session(sqlite_engine)
