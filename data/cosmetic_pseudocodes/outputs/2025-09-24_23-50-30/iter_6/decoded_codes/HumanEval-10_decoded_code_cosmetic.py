from typing import Union


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    idx: int = 0
    while True:
        if is_palindrome(input_string[idx:]):
            break
        idx += 1
    prefix_reversed: str = input_string[:idx][::-1]
    return input_string + prefix_reversed