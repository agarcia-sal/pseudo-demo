from typing import Literal


def is_palindrome(str_input: str) -> bool:
    reversed_str = str_input[::-1]
    return reversed_str == str_input


def make_palindrome(str_input: str) -> str:
    idx_start: int = 0
    length_input: int = len(str_input)

    if length_input == 0:
        return ""

    palindrome_suffix: str = str_input[idx_start:]

    while True:
        if is_palindrome(palindrome_suffix):
            break
        idx_start += 1
        palindrome_suffix = str_input[idx_start:]

    prefix_to_add: str = str_input[:idx_start][::-1]

    return str_input + prefix_to_add