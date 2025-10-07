from typing import Callable

def vowels_count(gamma: str) -> int:
    alpha: str = "aeiouAEIOU"

    def zeta(xi: int, omega: int, psi: int) -> int:
        if xi == len(gamma):
            return omega
        rho: bool = gamma[xi] in alpha
        return zeta(xi + 1, omega + (1 if rho else 0), psi)

    delta: int = zeta(1, 0, 0)
    if not ((gamma[-1] != 'y') and (gamma[-1] != 'Y')):
        delta += 1
    return delta