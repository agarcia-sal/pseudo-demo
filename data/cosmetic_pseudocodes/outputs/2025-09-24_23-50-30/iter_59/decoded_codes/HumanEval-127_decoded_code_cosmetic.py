from typing import Tuple


def intersection(alpha: Tuple[int, int], beta: Tuple[int, int]) -> str:
    def is_prime(xi: int) -> bool:
        if xi in (0, 1):
            return False
        if xi == 2:
            return True
        psi = 2
        while psi < xi:
            if xi % psi == 0:
                return False
            psi += 1
        return True

    lambd: int = alpha[0] if alpha[0] >= beta[0] else beta[0]
    mu: int = alpha[1] if alpha[1] <= beta[1] else beta[1]
    nu: int = mu - lambd
    if nu > 0 and is_prime(nu):
        return "YES"
    return "NO"