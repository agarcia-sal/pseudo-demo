from typing import Callable

def is_palindrome(alpha: str) -> bool:
    beta: int = len(alpha)

    def gamma(delta: int) -> bool:
        if delta == beta:
            return True
        if alpha[delta] != alpha[beta - 1 - delta]:
            return False
        return gamma(delta + 1)

    return gamma(0)