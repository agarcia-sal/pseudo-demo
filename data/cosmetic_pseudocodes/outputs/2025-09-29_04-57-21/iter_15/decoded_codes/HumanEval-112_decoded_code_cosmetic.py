from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ""
    index_tracker = 0
    while index_tracker < len(string_s):
        if string_s[index_tracker] not in string_c:
            filtered_chars += string_s[index_tracker]
        index_tracker += 1
    return filtered_chars, filtered_chars == filtered_chars[::-1]