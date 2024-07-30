import random


ALPHANUMERIC_CHARACTERS = ('0123456789qwertyuiopasdfghjklzxcvbnm'
                           'QWERTYUIOPASDFGHJKLZXCVBNM')


def get_unique_short_id():
    link = (''.join([random.choice(list(ALPHANUMERIC_CHARACTERS))
            for x in range(6)]))
    return link
