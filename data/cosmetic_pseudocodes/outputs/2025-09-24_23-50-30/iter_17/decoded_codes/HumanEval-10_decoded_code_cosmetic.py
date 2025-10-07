from typing import Dict


def is_palindrome(input_string: str) -> bool:
    left_index: int = 0
    right_index: int = len(input_string) - 1
    while left_index < right_index:
        if input_string[left_index] != input_string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    offset: int = 0
    # Find smallest offset such that substring input_string[offset:] is a palindrome
    while not is_palindrome(input_string[offset:]):
        offset += 1

    prefix_substring: str = input_string[:offset]
    reversed_prefix: str = "".join(prefix_substring[i] for i in range(len(prefix_substring) - 1, -1, -1))

    return input_string + reversed_prefix