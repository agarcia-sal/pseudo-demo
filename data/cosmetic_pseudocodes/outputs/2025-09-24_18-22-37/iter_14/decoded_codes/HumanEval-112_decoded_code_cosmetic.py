from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    result_string = ""
    idx = 0

    while idx < len(string_s):
        current_char = string_s[idx]
        if current_char not in string_c:
            result_string += current_char
        idx += 1

    reversed_string = ""
    rev_idx = len(result_string) - 1

    while rev_idx >= 0:
        reversed_string += result_string[rev_idx]
        rev_idx -= 1

    is_palindrome = reversed_string == result_string

    return result_string, is_palindrome