from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    filtered_s = ''.join(char for char in s if char not in c)
    is_palindrome = filtered_s == filtered_s[::-1]
    return filtered_s, is_palindrome