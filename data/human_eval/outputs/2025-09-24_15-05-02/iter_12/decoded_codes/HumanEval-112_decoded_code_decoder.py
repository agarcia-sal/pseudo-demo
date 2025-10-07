from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_s = ""
    for character in string_s:
        if character not in string_c:
            filtered_s += character
    is_palindrome = filtered_s == filtered_s[::-1]
    return filtered_s, is_palindrome