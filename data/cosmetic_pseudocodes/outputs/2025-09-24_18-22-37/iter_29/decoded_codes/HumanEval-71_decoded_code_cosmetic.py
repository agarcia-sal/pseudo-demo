from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if (alpha + beta) <= gamma or (alpha + gamma) <= beta or (beta + gamma) <= alpha:
        return -1.0

    omega: float = (alpha + beta + gamma) / 2
    psi: float = omega - alpha
    chi: float = omega - beta
    phi: float = omega - gamma

    xi: float = omega * psi
    eps: float = xi * chi
    delta: float = eps * phi

    zeta: float = round(sqrt(delta), 2)
    return zeta