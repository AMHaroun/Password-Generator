'''
Password Generator
-------------------------------------------------------------
Take's a length and returns a random password of that length
'''


import secrets
import string


def create_pw(pw_length=12):
    if pw_length == 1:
        return "Password length of 1 is not secure."

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True

    return pwd
