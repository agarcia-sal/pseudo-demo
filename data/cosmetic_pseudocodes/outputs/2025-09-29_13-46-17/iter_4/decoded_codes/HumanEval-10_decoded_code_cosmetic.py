from typing import Callable


def is_palindrome(input_string: str) -> bool:
    reversed_version = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_version += input_string[i]
    return reversed_version == input_string


def make_palindrome(input_string: str) -> str:
    def helper_palindrome_start(index: int) -> int:
        if index == len(input_string):
            return index
        suffix = input_string[index:]
        if is_palindrome(suffix):
            return index
        return helper_palindrome_start(index + 1)

    if len(input_string) == 0:
        return ""

    start_index = helper_palindrome_start(0)
    prefix_to_reverse = input_string[:start_index]
    reversed_prefix = ""
    for j in range(len(prefix_to_reverse) - 1, -1, -1):
        reversed_prefix += prefix_to_reverse[j]

    return input_string + reversed_prefix