from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    filtered_chars = [char for char in s if char not in c]
    s = ''.join(filtered_chars)
    reversed_s = ''
    index = len(s) - 1
    while index >= 0:
        reversed_s += s[index]
        index -= 1
    is_palindrome = reversed_s == s
    return s, is_palindrome