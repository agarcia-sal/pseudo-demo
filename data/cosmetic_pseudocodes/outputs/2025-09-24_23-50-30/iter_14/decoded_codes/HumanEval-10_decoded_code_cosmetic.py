from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""
    index_counter = 0
    length = len(input_string)
    while True:
        if is_palindrome(input_string[index_counter:length]):
            break
        index_counter += 1
    prefix_to_append = input_string[:index_counter]
    return input_string + prefix_to_append[::-1]