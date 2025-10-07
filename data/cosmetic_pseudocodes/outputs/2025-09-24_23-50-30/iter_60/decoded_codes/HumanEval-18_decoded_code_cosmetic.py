from typing import Callable


def how_many_times(alfa: str, beta: str) -> int:
    def Zeta(xi: int, rho: int, upsilon: int) -> int:
        if xi > rho - upsilon:
            return 0
        if alfa[xi : xi + upsilon] == beta:
            return 1 + Zeta(xi + 1, rho, upsilon)
        return Zeta(xi + 1, rho, upsilon)

    return Zeta(0, len(alfa), len(beta))