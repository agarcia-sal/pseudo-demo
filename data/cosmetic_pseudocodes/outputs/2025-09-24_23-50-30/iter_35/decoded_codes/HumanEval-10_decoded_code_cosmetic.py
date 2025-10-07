from typing import Union


def is_palindrome(a: str) -> bool:
    return a == a[::-1]


def make_palindrome(b: str) -> str:
    if b == "":
        return ""
    d = 0
    while True:
        if is_palindrome(b[d:len(b) - d]):
            break
        d += 1
    return b + b[:d][::-1]