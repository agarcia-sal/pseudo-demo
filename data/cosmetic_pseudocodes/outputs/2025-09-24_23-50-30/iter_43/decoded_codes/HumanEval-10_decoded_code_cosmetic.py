from typing import Sequence

def is_palindrome(theta: Sequence[str]) -> bool:
    return theta == theta[::-1]

def make_palindrome(omega: str) -> str:
    if not omega:
        return ""
    alpha = 0
    beta = len(omega)
    while True:
        if is_palindrome(omega[alpha:beta]):
            break
        alpha += 1
    gamma = omega[:alpha]
    return omega + gamma[::-1]