from typing import Tuple

def reverse_delete(str_input: str, str_filter: str) -> Tuple[str, bool]:
    temp_result = ""
    idx = 0
    while idx < len(str_input):
        curr_char = str_input[idx]
        if curr_char not in str_filter:
            temp_result += curr_char
        idx += 1

    reversed_temp = ""
    rev_idx = len(temp_result) - 1
    while rev_idx >= 0:
        reversed_temp += temp_result[rev_idx]
        rev_idx -= 1

    is_palindrome = (temp_result == reversed_temp)
    return temp_result, is_palindrome