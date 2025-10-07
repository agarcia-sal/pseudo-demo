from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""

    pal_suffix_start: int = 0

    while True:
        if is_palindrome(input_string[pal_suffix_start:]):
            break
        pal_suffix_start += 1

    return input_string + input_string[:pal_suffix_start][::-1]