from fast.core.bcrypt import hash_password, check_password


def test_check_valid_password():
    pw: str = 'dalmo123'
    hash: bytes = hash_password(pw)
    check: bool = check_password(pw, hash)
    assert check is True


def test_check_not_valid_password():
    pw_primary: str = 'dalmo123'
    hash_primary: bytes = hash_password(pw_primary)

    pw_secondary: str = '321dalmo'
    hash_secondary: bytes = hash_password(pw_secondary)
    
    primary: bool = check_password(pw_primary, hash_secondary)
    secondary: bool = check_password(pw_secondary, hash_primary)
    
    assert primary == secondary and hash_primary != hash_secondary
