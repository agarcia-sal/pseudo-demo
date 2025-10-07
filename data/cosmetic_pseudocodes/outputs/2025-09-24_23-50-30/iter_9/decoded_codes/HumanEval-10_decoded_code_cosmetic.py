from typing import List


def is_palindrome(alpha: str) -> bool:
    return alpha == alpha[::-1]


def make_palindrome(beta: str) -> str:
    if not beta:
        return ""
    start_idx = 0
    while not is_palindrome(beta[start_idx:]):
        start_idx += 1
    return beta + beta[:start_idx][::-1]