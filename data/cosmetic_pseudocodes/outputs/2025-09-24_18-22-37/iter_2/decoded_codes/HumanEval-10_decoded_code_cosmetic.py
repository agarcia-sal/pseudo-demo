from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    index: int = 0
    while True:
        if is_palindrome(input_string[index:]):
            break
        index += 1
    prefix: str = input_string[:index]
    suffix_reversed: str = prefix[::-1]
    return input_string + suffix_reversed