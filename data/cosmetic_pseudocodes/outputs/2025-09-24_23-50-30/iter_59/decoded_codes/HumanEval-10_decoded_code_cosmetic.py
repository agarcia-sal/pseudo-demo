from typing import Sequence

def is_palindrome(c1: Sequence[str]) -> bool:
    return c1 == c1[::-1]

def make_palindrome(d2: str) -> str:
    if d2 == "":
        return ""
    e3 = 0
    while True:
        if is_palindrome(d2[e3:]):
            break
        e3 += 1
    return d2 + d2[:e3][::-1]