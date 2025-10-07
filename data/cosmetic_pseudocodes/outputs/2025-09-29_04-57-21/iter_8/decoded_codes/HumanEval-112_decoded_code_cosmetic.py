from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = []
    idx = 0
    while idx < len(string_s):
        ch = string_s[idx]
        if ch not in string_c:
            filtered_chars.append(ch)
        idx += 1

    new_str = ''.join(filtered_chars)
    is_palindrome = new_str == new_str[::-1]
    return new_str, is_palindrome