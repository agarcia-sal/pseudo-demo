from typing import Optional


def is_palindrome(str_param: str) -> bool:
    reversed_str: str = str_param[::-1]
    equality_check: bool = str_param == reversed_str
    return equality_check


def make_palindrome(data_input: str) -> str:
    if not data_input:
        return ""
    idx_marker: int = 0
    check_substring: str = data_input[idx_marker:]
    while True:
        if is_palindrome(check_substring):
            break
        else:
            idx_marker += 1
            check_substring = data_input[idx_marker:]
    prefix_substring: str = data_input[:idx_marker]
    reversed_prefix: str = prefix_substring[::-1]
    result_string: str = data_input + reversed_prefix
    return result_string