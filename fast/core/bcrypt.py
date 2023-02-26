import bcrypt


def hash_password(password_text: str) -> bytes:
    passwd = bytes(password_text, encoding='UTF-8')
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def check_password(password_text: str, hash_password: bytes) -> bool:
    passwd = bytes(password_text, encoding='UTF-8')
    hash = bytes(hash_password, encoding='UTF-8')
    if bcrypt.checkpw(passwd, hash):
        return True
    return False
