from typing import Literal


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def make_palindrome(str: str) -> str:
    if str == "":
        return ""
    suffix_start_index = 0
    while not is_palindrome(str[suffix_start_index:]):
        suffix_start_index += 1
    return str + str[:suffix_start_index][::-1]