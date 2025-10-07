from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not ((alpha + beta > gamma) and (alpha + gamma > beta) and (beta + gamma > alpha)):
        return -1
    delta: float = (alpha + beta + gamma) * 0.5
    epsilon: float = sqrt(delta * (delta - alpha) * (delta - beta) * (delta - gamma))
    zeta: float = round(epsilon * 100) / 100
    return zeta