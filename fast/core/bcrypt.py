import bcrypt


def hash_password(password_text: str) -> bytes:
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(password_text.encode('utf-8'), salt)
    return hashed


def check_password(password_text: str, hash_password: str | bytes) -> bool:
    if type(hash_password) == str:
        hash_password = hash_password.encode('utf-8')

    if bcrypt.checkpw(password_text.encode('utf-8'), hash_password):
        return True
    return False
