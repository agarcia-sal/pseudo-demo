from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, str]:
    filtered_chars: list[str] = []
    index_tracker: int = 0
    while index_tracker < len(string_s):
        current_char: str = string_s[index_tracker]
        if current_char not in string_c:
            filtered_chars.append(current_char)
        index_tracker += 1
    string_s = ''.join(filtered_chars)

    reversed_s: str = ''
    rev_index: int = len(string_s) - 1
    while rev_index >= 0:
        reversed_s += string_s[rev_index]
        rev_index -= 1

    return string_s, reversed_s