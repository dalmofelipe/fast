from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from fast.models import user
from fast.infra.config import settings

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


STRING_CONN = ''
ENVIRONMENT = settings['ENVIRONMENT']

if ENVIRONMENT.upper() == 'PROD':
    #STRING_CONN = settings.db.prod
    DB_HOST = settings['DB_HOST']
    DB_PORT = settings['DB_PORT']
    DB_NAME = settings['DB_NAME']
    DB_USER = settings['DB_USER']
    DB_PASS = settings['DB_PASS']
    STRING_CONN = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'
else:
    STRING_CONN = settings['DB_DEV']


engine = create_engine(STRING_CONN, echo=False)
user.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
