from typing import Optional


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if not string:
        return ""

    beginning_of_suffix = 0
    length = len(string)

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
        if beginning_of_suffix > length:  # edge case safety
            break

    return string + string[:beginning_of_suffix][::-1]