from typing import Literal


def is_palindrome(string_arg: str) -> bool:
    return string_arg == string_arg[::-1]


def make_palindrome(str_param: str) -> str:
    if str_param == "":
        return ""

    idx_marker: int = 0
    length = len(str_param)
    while True:
        if is_palindrome(str_param[idx_marker:length]):
            break
        idx_marker += 1

    return str_param + str_param[:idx_marker][::-1]