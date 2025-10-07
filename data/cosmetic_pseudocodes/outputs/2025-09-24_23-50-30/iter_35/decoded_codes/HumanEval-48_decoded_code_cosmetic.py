from typing import Sequence

def is_palindrome(beta: Sequence[str]) -> bool:
    omega: int = len(beta)
    i: int = 0
    while i < omega:
        if beta[i] != beta[omega - 1 - i]:
            return False
        i += 1
    return True