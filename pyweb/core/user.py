from pyweb.database.config import get_session
from pyweb.models.user import User


def save_user_on_db(
    name:str, 
    email:str, 
    password:str
):
    """
    """
    user = User()
    user.name = name 
    user.email = email
    user.password = password # bcryptar essa senha!
    
    with get_session() as session:
        session.add(user)
        session.commit()
