from typing import Tuple

def reverse_delete(string_p: str, string_q: str) -> Tuple[str, bool]:
    temp_str = ''
    iter_idx = 0
    limit_idx = len(string_p)
    while iter_idx < limit_idx:
        current_char = string_p[iter_idx]
        if current_char not in string_q:
            temp_str += current_char
        iter_idx += 1

    reversed_temp_str = ''
    rev_idx = len(temp_str) - 1
    while rev_idx >= 0:
        reversed_temp_str += temp_str[rev_idx]
        rev_idx -= 1

    is_palindrome = (reversed_temp_str == temp_str)
    return temp_str, is_palindrome