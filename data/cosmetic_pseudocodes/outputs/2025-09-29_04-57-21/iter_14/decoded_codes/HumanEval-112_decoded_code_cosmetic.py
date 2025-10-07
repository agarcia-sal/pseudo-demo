from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = []
    idx = 0
    while idx < len(string_s):
        current_char = string_s[idx]
        if current_char not in string_c:
            filtered_chars.append(current_char)
        idx += 1
    processed_str = ''.join(filtered_chars)
    is_palindrome_flag = processed_str == processed_str[::-1]
    return processed_str, is_palindrome_flag