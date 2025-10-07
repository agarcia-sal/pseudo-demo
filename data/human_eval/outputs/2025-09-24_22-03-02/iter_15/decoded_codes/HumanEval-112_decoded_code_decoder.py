from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    original_s = s
    s = ''
    for char in original_s:
        if char not in c:
            s += char
    reversed_s = ''
    for index in range(len(s) - 1, -1, -1):
        reversed_s += s[index]
    is_palindrome = reversed_s == s
    return s, is_palindrome