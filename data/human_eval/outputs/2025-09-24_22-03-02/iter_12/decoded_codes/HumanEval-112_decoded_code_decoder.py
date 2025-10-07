from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    s = ''.join(char for char in s if char not in c)
    is_palindrome = s == s[::-1]
    return s, is_palindrome