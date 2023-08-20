import secrets
import string

def referral_key_generator(length):
    '''Генерация реферального кода'''
    characters = string.ascii_uppercase + string.digits
    key = ''.join(secrets.choice(characters) for _ in range(length))
    return key


def phone_key_generator(length):
    '''Генерация кода авторизации'''
    characters = string.digits 
    key = ''.join(secrets.choice(characters) for _ in range(length))
    return key