from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    temp_str = ''
    idx = 0

    while idx < len(string_s):
        curr_char = string_s[idx]
        if curr_char not in string_c:
            temp_str += curr_char
        idx += 1

    rev_str = ''
    rev_idx = len(temp_str) - 1

    while rev_idx >= 0:
        rev_str += temp_str[rev_idx]
        rev_idx -= 1

    is_palindrome = rev_str == temp_str

    return temp_str, is_palindrome