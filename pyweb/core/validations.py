import re

from typing import Dict, Union

from pyweb.models.user import User

# Regex simples para validar Emails
REGEX_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

 
def check_email(email):
    """
    """
    if(re.fullmatch(REGEX_EMAIL, email)):
        return True
 
    return False



def user_input_form_data_is_valid(
    name, 
    email, 
    password, 
    confirm
) -> Union[bool,Dict]:
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
        errors['name_error'] = "O nome de conter entre 3 e 20 caracteres"

    if not check_email(email):
        errors['email_error'] = "Email inválido"

    if len(password) < 8 or len(password) > 12:
        errors['password_error'] = "Deve ter no minimo 8 e o maximo 12 caracteres"

    if password != confirm:
        errors['confirm_error'] = "As senhas não conferem"

    if len(errors) > 0:
        return False, errors

    return True, {}
