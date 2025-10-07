from typing import Union


def is_palindrome(input_string: str) -> bool:
    reversed_str = input_string[::-1]
    return input_string == reversed_str


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    idx = 0
    while True:
        candidate = input_string[idx:]
        if is_palindrome(candidate):
            break
        idx += 1

    prefix_to_add = input_string[:idx]
    palindrome_result = input_string + prefix_to_add[::-1]
    return palindrome_result