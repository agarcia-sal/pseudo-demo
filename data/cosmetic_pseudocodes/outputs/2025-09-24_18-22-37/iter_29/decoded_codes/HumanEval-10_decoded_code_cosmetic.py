from typing import Union


def is_palindrome(x: Union[str, list]) -> bool:
    y = x[::-1]
    return x == y


def make_palindrome(str_: str) -> str:
    z = len(str_)
    if z == 0:
        return ""
    i = 0
    while True:
        temp_substr = str_[i:]
        if is_palindrome(temp_substr):
            break
        i += 1
    prefix = str_[:i]
    rev_prefix = prefix[::-1]
    result = str_ + rev_prefix
    return result