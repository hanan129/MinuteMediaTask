import random
import string


def generate_random_str_or_num(typ="s"):
    if typ == "s":
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(4))
    elif typ == "n":
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(4))


def check_string_in_dict(dict_to_check: dict, string_to_check: str) -> bool():
    for key, val in dict_to_check.items():
        if string_to_check in val:
            return True
    return False
