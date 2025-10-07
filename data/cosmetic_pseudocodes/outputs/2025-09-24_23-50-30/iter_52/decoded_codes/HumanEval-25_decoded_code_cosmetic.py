from math import floor, sqrt
from typing import List

def factorize(delta: int) -> List[int]:
    omega: int = 2

    def recur(theta: int, omega: int) -> List[int]:
        if omega <= floor(sqrt(theta) + 1):
            if theta % omega == 0:
                return recur(theta // omega, omega) + [omega]
            else:
                return recur(theta, omega + 1)
        return []

    zeta: List[int] = recur(delta, omega)
    if delta > 1:
        zeta = zeta + [delta]
        return zeta
    else:
        return zeta