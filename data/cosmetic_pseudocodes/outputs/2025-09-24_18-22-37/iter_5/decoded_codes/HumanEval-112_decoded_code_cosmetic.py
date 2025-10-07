from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = "".join(ch for ch in string_s if ch not in string_c)
    reversed_filtered = filtered_chars[::-1]
    is_palindrome = reversed_filtered == filtered_chars
    return filtered_chars, is_palindrome