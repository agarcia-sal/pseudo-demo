from typing import Optional

def is_palindrome(str_arg: str) -> bool:
    reversed_str: str = str_arg[::-1]
    temp_bool: bool = str_arg == reversed_str
    return temp_bool

def make_palindrome(str_val: str) -> str:
    idx_start: int = 0

    if str_val == "":
        return ""

    while True:
        if is_palindrome(str_val[idx_start:]):
            break
        idx_start += 1

    prefix_part: str = str_val[:idx_start]
    suffix_to_append: str = prefix_part[::-1]

    return str_val + suffix_to_append