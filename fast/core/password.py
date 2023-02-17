import bcrypt


def hash_password(password_text:str) -> bytes:
    passwd = bytes(password_text, encoding='UTF-8')
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def check_password(hash_password:bytes, password_text:str) -> bool:
    passwd = bytes(password_text, encoding='UTF-8')
    if bcrypt.checkpw(passwd, hash_password):
        return True
    return False
