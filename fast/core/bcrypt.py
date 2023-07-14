import bcrypt


def hash_password(password_text: str) -> bytes:
    passwd = bytes(password_text, encoding='UTF-8')
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def check_password(password_text: str, hash_password: str) -> bool:
    passwd = bytes(password_text, encoding='UTF-8')
    hash_password = bytes(hash_password)
    if bcrypt.checkpw(passwd, hash_password):
        return True
    return False
