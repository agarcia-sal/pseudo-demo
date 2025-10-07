from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ''
    index_position = 0
    while index_position < len(string_s):
        current_char = string_s[index_position]
        if current_char not in string_c:
            filtered_chars += current_char
        index_position += 1
    palindrome_check = (filtered_chars == filtered_chars[::-1])
    return filtered_chars, palindrome_check