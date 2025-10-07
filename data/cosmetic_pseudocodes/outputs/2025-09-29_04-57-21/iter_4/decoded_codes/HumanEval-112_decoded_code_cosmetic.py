from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars: list[str] = []
    idx: int = 0
    while idx < len(string_s):
        current_char: str = string_s[idx]
        if current_char not in string_c:
            filtered_chars.append(current_char)
        idx += 1
    string_s = ''.join(filtered_chars)
    reversed_str: str = ''
    rev_idx: int = len(string_s) - 1
    while rev_idx >= 0:
        reversed_str += string_s[rev_idx]
        rev_idx -= 1
    return string_s, reversed_str == string_s