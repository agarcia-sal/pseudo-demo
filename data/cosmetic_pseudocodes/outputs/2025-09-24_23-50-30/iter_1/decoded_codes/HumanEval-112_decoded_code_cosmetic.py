from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_chars = [char for char in string_s if char not in string_c]
    string_s = "".join(filtered_chars)
    is_palindrome = string_s == string_s[::-1]
    return string_s, is_palindrome