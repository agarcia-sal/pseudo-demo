from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    suffix_start_index = 0

    while True:
        candidate_substring = input_string[suffix_start_index:]
        if is_palindrome(candidate_substring):
            break
        suffix_start_index += 1

    prefix_segment = input_string[:suffix_start_index]
    return input_string + prefix_segment[::-1]