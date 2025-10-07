from typing import Literal

def is_palindrome(str_parameter: str) -> bool:
    reversed_version = str_parameter[::-1]
    return str_parameter == reversed_version

def make_palindrome(str_parameter: str) -> str:
    if not str_parameter:
        return ""
    index_marker = 0
    length = len(str_parameter)
    while True:
        suffix_substring = str_parameter[index_marker:length]
        if is_palindrome(suffix_substring):
            break
        index_marker += 1
    prefix_substring = str_parameter[:index_marker]
    reversed_prefix = prefix_substring[::-1]
    return str_parameter + reversed_prefix