from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    idx: int = 0
    if idx >= len(input_string):
        return ""
    while idx < len(input_string):
        if is_palindrome(input_string[idx:]):
            break
        idx += 1
    return input_string + input_string[:idx][::-1]