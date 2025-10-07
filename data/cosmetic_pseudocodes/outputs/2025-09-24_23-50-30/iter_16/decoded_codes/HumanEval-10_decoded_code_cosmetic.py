from typing import Literal


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""
    palindrome_suffix_start = 0
    length = len(input_string)
    while True:
        current_substring = input_string[palindrome_suffix_start:length]
        if is_palindrome(current_substring):
            break
        palindrome_suffix_start += 1
    prefix_part = input_string[:palindrome_suffix_start]
    reversed_prefix = prefix_part[::-1]
    return input_string + reversed_prefix