from typing import Any


def is_palindrome(zeta: str) -> bool:
    return zeta == zeta[::-1]


def make_palindrome(omega: str) -> str:
    if omega == "":
        return ""
    alpha = 0
    length = len(omega)
    # Increase alpha until substring omega[alpha:] is a palindrome
    while not is_palindrome(omega[alpha:length]):
        alpha += 1  # (1 - 0) is always 1
    # Append reversed prefix omega[:alpha] to omega
    return omega + omega[:alpha][::-1]