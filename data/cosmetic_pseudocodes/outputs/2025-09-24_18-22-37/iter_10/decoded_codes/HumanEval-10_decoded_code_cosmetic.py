from typing import Optional


def is_palindrome(text_input: str) -> bool:
    reversed_version: str = text_input[::-1]
    return reversed_version == text_input


def make_palindrome(source_string: str) -> str:
    if not source_string:
        return ""

    marker_counter: int = 0
    length: int = len(source_string)

    while marker_counter < length:
        suffix: str = source_string[marker_counter:]
        if is_palindrome(suffix):
            break
        marker_counter += 1

    prefix: str = source_string[:marker_counter]
    rev_prefix: str = prefix[::-1]

    return source_string + rev_prefix