from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if (alpha + beta) <= gamma or (alpha + gamma) <= beta or (beta + gamma) <= alpha:
        return -1
    delta: float = (alpha + beta + gamma) / 2
    epsilon: float = sqrt(delta * (delta - alpha) * (delta - beta) * (delta - gamma))
    zeta: float = round(epsilon, 2)
    return zeta