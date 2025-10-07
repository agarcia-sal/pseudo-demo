from typing import Union


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    index_marker: int = 0
    while not is_palindrome(input_string[index_marker:]):
        index_marker += 1
    if index_marker == 0:
        return input_string
    return input_string + input_string[:index_marker][::-1]