from math import sqrt
from typing import Union

def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    lam = (alpha + beta + gamma) / 2
    delta = sqrt(lam * (lam - alpha) * (lam - beta) * (lam - gamma))
    epsilon = round(delta * 100) / 100
    return epsilon