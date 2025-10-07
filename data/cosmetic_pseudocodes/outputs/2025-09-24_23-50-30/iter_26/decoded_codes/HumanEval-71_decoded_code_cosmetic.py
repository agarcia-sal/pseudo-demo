from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if (alpha + beta <= gamma) or (alpha + gamma <= beta) or (beta + gamma <= alpha):
        return -1
    psi = (alpha + beta + gamma) / 2
    delta = sqrt(psi * (psi - alpha) * (psi - beta) * (psi - gamma))
    omega = round(delta * 100) / 100
    return omega