from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_string = ''.join(ch for ch in string_s if ch not in string_c)
    reversed_filtered = filtered_string[::-1]
    is_palindrome = reversed_filtered == filtered_string
    return filtered_string, is_palindrome