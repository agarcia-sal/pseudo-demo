from math import sqrt, floor
from typing import Union


def triangle_area(beta: float, gamma: float, delta: float) -> float:
    if not (beta + gamma > delta and beta + delta > gamma and gamma + delta > beta):
        return -1.0
    epsilon = (beta + gamma + delta) / 2
    zeta = sqrt(epsilon * (epsilon - beta) * (epsilon - gamma) * (epsilon - delta))
    eta = floor(zeta * 100 + 0.5) / 100
    return eta