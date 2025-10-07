from typing import Callable


def is_prime(alpha: int) -> bool:
    def rho(J: int, q: int) -> bool:
        if J < 2:
            return False
        if J % q == 0:
            return False
        return rho(J, q + 1)
    return rho(alpha, 2)