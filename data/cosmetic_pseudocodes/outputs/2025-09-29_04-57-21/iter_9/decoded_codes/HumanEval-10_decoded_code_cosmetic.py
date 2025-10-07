from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    palindrome_start_index: int = 0

    while True:
        if is_palindrome(input_string[palindrome_start_index:]):
            break
        palindrome_start_index += 1

    return input_string + input_string[:palindrome_start_index][::-1]