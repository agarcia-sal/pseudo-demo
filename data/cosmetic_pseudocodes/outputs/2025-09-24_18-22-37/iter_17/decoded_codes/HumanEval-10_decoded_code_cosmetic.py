from typing import Literal


def is_palindrome(alpha: str) -> bool:
    omega: str = alpha[::-1]
    return alpha == omega


def make_palindrome(bravo: str) -> str:
    if len(bravo) == 0:
        return ""
    charlie: int = 0
    while True:
        delta: str = bravo[charlie:]
        if is_palindrome(delta):
            break
        charlie += 1
    echo: str = bravo[:charlie]
    return bravo + echo[::-1]