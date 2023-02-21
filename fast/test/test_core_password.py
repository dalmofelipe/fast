from fast.core.password import hash_password, check_password


def test_check_valid_password():
    hash: bytes = b''
    pw: str = 'dalmo123'
    hash: bytes = hash_password(pw)
    check: bool = check_password(hash, pw)
    assert check is True


def test_check_invalid_password():
    pw_original: str = 'dalmo123'
    hash_original: bytes = hash_password(pw_original)
    pw_incorrect: str = 'dalmo123123'
    hash_incorrect: bytes = hash_password(pw_incorrect)
    original: bool = check_password(hash_incorrect, pw_original)
    incorrect: bool = check_password(hash_original, pw_incorrect)
    # as duas tem que esta False
    assert original == incorrect
