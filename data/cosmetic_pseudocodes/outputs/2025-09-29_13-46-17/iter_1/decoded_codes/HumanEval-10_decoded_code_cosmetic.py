from typing import Literal


def is_palindrome(input_string: str) -> bool:
    reversed_string = input_string[::-1]
    return input_string == reversed_string


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    index = 0
    while True:
        suffix = input_string[index:]
        if is_palindrome(suffix):
            break
        index += 1
    prefix_to_append = input_string[:index]
    reversed_prefix = prefix_to_append[::-1]
    return input_string + reversed_prefix