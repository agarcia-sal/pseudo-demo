from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1.0
    sigma: float = (alpha + beta + gamma) / 2
    omega: float = sqrt(sigma * (sigma - alpha) * (sigma - beta) * (sigma - gamma))
    psi: float = round(omega * 100) / 100
    return psi