from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    omega = (alpha + beta + gamma) / 2
    zeta = omega * (omega - alpha) * (omega - beta) * (omega - gamma)
    eta = sqrt(zeta)
    xi = round(eta, 2)
    return xi