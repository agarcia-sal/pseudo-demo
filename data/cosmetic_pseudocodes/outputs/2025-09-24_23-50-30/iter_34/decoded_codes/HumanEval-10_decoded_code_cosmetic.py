from typing import Sequence

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    if len(s) == 0:
        return ""
    idx: int = 0
    while not is_palindrome(s[idx:]):
        idx += 1
    return s + s[:idx][::-1]