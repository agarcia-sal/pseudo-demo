from typing import Optional


def is_palindrome(string_parameter: str) -> bool:
    reversed_string: str = string_parameter[::-1]
    return reversed_string == string_parameter


def make_palindrome(string_parameter: str) -> str:
    if not string_parameter:
        return ""

    index_marker: int = 0
    length: int = len(string_parameter)

    while True:
        current_substring: str = string_parameter[index_marker:length]
        if is_palindrome(current_substring):
            break
        index_marker += 1

    prefix_substring: str = string_parameter[:index_marker]
    reversed_prefix: str = prefix_substring[::-1]
    return string_parameter + reversed_prefix