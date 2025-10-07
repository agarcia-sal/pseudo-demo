from typing import AnyStr

def is_happy(string_s: AnyStr) -> bool:
    if len(string_s) < 3:
        return False

    for index in range(len(string_s) - 2):
        if (string_s[index] == string_s[index + 1] or
            string_s[index + 1] == string_s[index + 2] or
            string_s[index] == string_s[index + 2]):
            return False

    return True