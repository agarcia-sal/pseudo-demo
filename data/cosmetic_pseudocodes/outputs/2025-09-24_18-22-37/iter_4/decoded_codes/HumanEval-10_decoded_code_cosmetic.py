from typing import Sequence

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    if len(s) == 0:
        return ""
    index_to_suffix = 0
    while True:
        suffix = s[index_to_suffix:]
        if is_palindrome(suffix):
            break
        index_to_suffix += 1
    prefix = s[:index_to_suffix]
    return s + prefix[::-1]