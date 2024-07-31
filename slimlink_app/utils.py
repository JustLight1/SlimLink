import random


ALPHANUMERIC_CHARACTERS = ('0123456789qwertyuiopasdfghjklzxcvbnm'
                           'QWERTYUIOPASDFGHJKLZXCVBNM')


def get_unique_short_id():
    link = (''.join([random.choice(list(ALPHANUMERIC_CHARACTERS))
            for x in range(6)]))
    return link


def check_custom_id(custom_id):
    for symbol in custom_id:
        if symbol not in ALPHANUMERIC_CHARACTERS:
            return False
    return True
