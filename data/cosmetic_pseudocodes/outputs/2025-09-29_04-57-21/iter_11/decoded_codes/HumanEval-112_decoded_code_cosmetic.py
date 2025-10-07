from typing import Tuple

def reverse_delete(str_m: str, str_n: str) -> Tuple[str, bool]:
    filtered_chars = []
    pos = 0
    while pos < len(str_m):
        curr_char = str_m[pos]
        if curr_char not in str_n:
            filtered_chars.append(curr_char)
        pos += 1
    filtered_str = ''.join(filtered_chars)
    is_palindrome = filtered_str == filtered_str[::-1]
    return filtered_str, is_palindrome