from typing import Literal


def is_palindrome(str_param: str) -> bool:
    reversed_str: str = ""
    idx: int = len(str_param) - 1

    while idx >= 0:
        reversed_str += str_param[idx]
        idx -= 1

    return str_param == reversed_str


def make_palindrome(word: str) -> str:
    if len(word) == 0:
        return ""

    suffix_start: int = 0
    continue_loop: bool = True

    while continue_loop:
        substring_val: str = ""
        pos: int = suffix_start

        while pos < len(word):
            substring_val += word[pos]
            pos += 1

        is_substring_palindrome: bool = is_palindrome(substring_val)
        if is_substring_palindrome:
            continue_loop = False
        else:
            suffix_start += 1

    prefix_substring: str = ""
    index: int = 0

    while index < suffix_start:
        prefix_substring += word[index]
        index += 1

    reversed_prefix: str = ""
    rev_index: int = len(prefix_substring) - 1

    while rev_index >= 0:
        reversed_prefix += prefix_substring[rev_index]
        rev_index -= 1

    result_palindrome: str = word + reversed_prefix
    return result_palindrome