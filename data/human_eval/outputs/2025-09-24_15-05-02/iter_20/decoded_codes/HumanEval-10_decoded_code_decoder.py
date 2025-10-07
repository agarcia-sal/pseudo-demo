from typing import Optional


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if not string:
        return ""

    beginning_of_suffix: int = 0

    # Find the smallest suffix starting at beginning_of_suffix which is a palindrome
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]