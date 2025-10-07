from typing import Callable


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    def seek_pal_suffix(start_index: int) -> int:
        if start_index >= len(input_string):
            return start_index
        if is_palindrome(input_string[start_index:]):
            return start_index
        return seek_pal_suffix(start_index + 1)

    suffix_start = seek_pal_suffix(0)
    return input_string + input_string[:suffix_start][::-1]