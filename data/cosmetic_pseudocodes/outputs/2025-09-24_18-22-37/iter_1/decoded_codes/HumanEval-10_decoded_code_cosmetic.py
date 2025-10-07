from typing import Sequence


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""
    suffix_start_index: int = 0
    length: int = len(input_string)
    while not is_palindrome(input_string[suffix_start_index:length]):
        suffix_start_index += 1
    prefix_to_add: str = input_string[:suffix_start_index]
    return input_string + prefix_to_add[::-1]