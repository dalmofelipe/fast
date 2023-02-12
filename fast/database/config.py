from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from fast.models import user

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine('sqlite:///fast/database/database.sqlite', echo=False)
user.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
