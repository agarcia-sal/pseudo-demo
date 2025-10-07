from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = ''.join(char for char in string_s if char not in string_c)
    is_palindrome = filtered_chars == filtered_chars[::-1]
    return filtered_chars, is_palindrome