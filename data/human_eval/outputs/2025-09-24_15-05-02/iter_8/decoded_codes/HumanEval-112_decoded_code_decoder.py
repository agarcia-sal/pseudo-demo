from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_string = ''.join(ch for ch in string_s if ch not in string_c)
    is_palindrome = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome