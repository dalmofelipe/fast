from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from fast.models import user
from fast.config.environment import Settings

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine(Settings.DB_STRING_CONN, echo=False)
user.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
