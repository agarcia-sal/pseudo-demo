from typing import List


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def make_palindrome(s: str) -> str:
    if s:
        idx = 0
        length = len(s)
        while not is_palindrome(s[idx:length]):
            idx += 1
        return s + s[:idx][::-1]
    else:
        return ""