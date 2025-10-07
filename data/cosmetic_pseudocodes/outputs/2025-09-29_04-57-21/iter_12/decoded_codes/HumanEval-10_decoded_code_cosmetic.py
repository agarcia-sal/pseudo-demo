from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    reversed_version = ""
    idx = len(input_string) - 1
    while idx >= 0:
        reversed_version += input_string[idx]
        idx -= 1
    return reversed_version == input_string


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    suffix_start_index = 0
    while True:
        substring_candidate = input_string[suffix_start_index:]
        if is_palindrome(substring_candidate):
            break
        suffix_start_index += 1

    prefix_part = input_string[:suffix_start_index]
    reversed_prefix = ""
    i = len(prefix_part) - 1
    while i >= 0:
        reversed_prefix += prefix_part[i]
        i -= 1

    return input_string + reversed_prefix