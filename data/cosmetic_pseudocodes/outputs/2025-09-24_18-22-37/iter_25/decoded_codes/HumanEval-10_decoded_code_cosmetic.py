from typing import List


def is_palindrome(alpha: str) -> bool:
    gamma: str = alpha[::-1]
    return alpha == gamma


def make_palindrome(omega: str) -> str:
    if omega == "":
        return ""
    sigma: int = 0
    while True:
        delta: str = omega[sigma:]
        if is_palindrome(delta):
            break
        sigma += 1
    epsilon: str = omega[:sigma]
    zeta: str = epsilon[::-1]
    result: str = omega + zeta
    return result