from typing import AnyStr


def is_palindrome(alpha: str) -> bool:
    return alpha == alpha[::-1]


def make_palindrome(beta: str) -> str:
    if beta == "":
        return ""

    theta = 0
    while True:
        if is_palindrome(beta[theta:]):
            break
        theta += 1

    omega = beta[:theta]
    return beta + omega[::-1]