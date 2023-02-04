from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from pyweb.models import user

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine('sqlite:///pyweb/database/database.sqlite', echo=False)
user.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
