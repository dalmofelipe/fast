import re

from typing import Dict, Union


# Regex simples para validar Emails
REGEX_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check_email(email):
    """ """
    if re.fullmatch(REGEX_EMAIL, email):
        return True

    return False


def user_data(name, email, password, confirm) -> Union[bool, Dict]:
    """ 
    Valida informações enviadas pelo formulário de registro da webapp

    A cada validação, adiciona um erro nomeado num dicionario de erros, caso
    infrinja a restrição

    Input: nome, email, password (sem hash) e confirmação da senha (sem hash)

    Output: Uma bandeira booleana informando que houve erros ou não, e um
    dicionário com erros nomeados 
    """
    errors = {}

    if len(name) < 3 or len(name) > 20:
        errors['name'] = 'O nome de conter entre 3 e 20 caracteres'

    if not check_email(email):
        errors['email'] = f'O email "{email}" é inválido'

    if len(password) < 6 or len(password) > 12:
        errors['password'] = 'A senha deve ter entre 6 e 12 caracteres'

    if password != confirm:
        errors[
            'confirm_pass'
        ] = 'A senha e a confirmação estão diferentes'

    if len(errors) > 0:
        return False, errors

    return True, {}
