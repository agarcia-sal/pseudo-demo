from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    index_pal_suffix = 0
    while not is_palindrome(input_string[index_pal_suffix:]):
        index_pal_suffix += 1
    return input_string + input_string[:index_pal_suffix][::-1]