from typing import Literal


def is_palindrome(test_str: str) -> bool:
    reversed_str = test_str[::-1]
    return reversed_str == test_str


def make_palindrome(source_str: str) -> str:
    if len(source_str) == 0:
        return ""

    start_index = 0
    palindrome_found: bool = False

    while not palindrome_found:
        substring_check = source_str[start_index:]
        if is_palindrome(substring_check):
            palindrome_found = True
        else:
            start_index += 1

    prefix = source_str[:start_index]
    reversed_prefix = prefix[::-1]

    return source_str + reversed_prefix