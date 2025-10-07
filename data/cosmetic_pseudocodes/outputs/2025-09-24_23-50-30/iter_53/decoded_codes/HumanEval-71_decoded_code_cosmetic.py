from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1.0
    delta: float = (alpha + beta + gamma) / 2
    epsilon: float = delta * (delta - alpha) * (delta - beta) * (delta - gamma)
    zeta: float = sqrt(epsilon)
    eta: float = round(zeta, 2)
    return eta