from typing import Sequence


def is_palindrome(alpha: Sequence[str]) -> bool:
    omega: int = len(alpha)
    beta: int = 0
    while beta < omega:
        gamma: int = omega - 1 - beta
        if alpha[beta] != alpha[gamma]:
            return False
        beta += 1
    return True