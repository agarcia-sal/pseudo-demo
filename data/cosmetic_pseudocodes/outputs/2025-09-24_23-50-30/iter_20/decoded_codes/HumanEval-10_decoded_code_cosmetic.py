from typing import Literal


def is_palindrome(alpha: str) -> bool:
    delta: str = alpha[::-1]  # reverse string
    return alpha == delta


def make_palindrome(omega: str) -> str:
    if not omega:
        return ""

    epsilon: int = 0
    length: int = len(omega)
    while not is_palindrome(omega[epsilon:length]):
        epsilon += 1

    zeta: str = omega[:epsilon]
    eta: str = zeta[::-1]
    return omega + eta