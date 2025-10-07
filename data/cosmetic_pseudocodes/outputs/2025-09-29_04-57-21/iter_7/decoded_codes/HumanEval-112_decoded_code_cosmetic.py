from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ""
    index_pos = 1
    while index_pos <= len(string_s):
        if string_s[index_pos - 1] not in string_c:
            filtered_chars += string_s[index_pos - 1]
        index_pos += 1
    return filtered_chars, filtered_chars == filtered_chars[::-1]