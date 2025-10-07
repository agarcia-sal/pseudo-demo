from typing import Optional


def is_palindrome(input_string: str) -> bool:
    temp_var = input_string[::-1]
    flag = input_string == temp_var
    return flag


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""
    idx_marker = 0
    length = len(input_string)
    while True:
        candidate_substring = input_string[idx_marker:length]
        if is_palindrome(candidate_substring):
            break
        idx_marker += 1
    prefix_to_append = input_string[:idx_marker]
    reversed_prefix = prefix_to_append[::-1]
    result_string = input_string + reversed_prefix
    return result_string