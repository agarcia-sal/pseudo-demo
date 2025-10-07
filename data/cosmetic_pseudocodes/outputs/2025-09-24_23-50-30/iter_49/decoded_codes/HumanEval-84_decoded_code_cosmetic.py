from typing import Optional

def solve(delta: int) -> str:
    def loop_gamma(zeta: int, epsilon: str) -> int:
        if not epsilon:
            return zeta
        return loop_gamma(zeta + int(epsilon[0]), epsilon[1:])

    omega = loop_gamma(0, str(delta))
    psi = bin(omega)[2:]
    return psi