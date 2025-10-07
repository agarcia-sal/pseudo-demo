from typing import Optional


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if not string:
        return ""
    beginning_of_suffix = 0
    length = len(string)
    # Increment beginning_of_suffix until the suffix string[beginning_of_suffix:] is a palindrome
    while beginning_of_suffix < length and not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    # Concatenate original string with the reversed prefix that is before the palindrome suffix
    return string + string[:beginning_of_suffix][::-1]