from typing import AnyStr


def is_palindrome(input_string: str) -> bool:
    reversed_buffer: str = ""
    for index in range(len(input_string) - 1, -1, -1):
        reversed_buffer += input_string[index]
    return reversed_buffer == input_string


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    suffix_start_index: int = 0
    while True:
        tail_substring = input_string[suffix_start_index:]
        if is_palindrome(tail_substring):
            break
        suffix_start_index += 1

    prefix_to_append = input_string[:suffix_start_index]
    reversed_prefix = ""
    for position in range(len(prefix_to_append) - 1, -1, -1):
        reversed_prefix += prefix_to_append[position]

    return input_string + reversed_prefix