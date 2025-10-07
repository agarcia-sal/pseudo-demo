from typing import Union


def fibfib(alpha: int) -> int:
    if alpha == 0:
        return 0
    if alpha == 1:
        return 0
    if alpha == 2:
        return 1

    omega: int = 1
    psi: int = 2
    theta: int = 3

    delta: int = alpha - omega
    epsilon: int = alpha - psi
    zeta: int = alpha - theta

    result: int = fibfib(delta) + fibfib(epsilon) + fibfib(zeta)

    return result