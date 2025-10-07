from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_string = ""
    idx = 0
    while idx < len(string_s):
        current_char = string_s[idx]
        if current_char not in string_c:
            filtered_string += current_char
        idx += 1

    reversed_string = ""
    rev_idx = len(filtered_string) - 1
    while rev_idx >= 0:
        reversed_string += filtered_string[rev_idx]
        rev_idx -= 1

    is_palindrome = filtered_string == reversed_string

    return filtered_string, is_palindrome