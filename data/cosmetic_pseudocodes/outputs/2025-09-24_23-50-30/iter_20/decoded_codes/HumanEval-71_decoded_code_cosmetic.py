from math import sqrt
from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    delta: float = (alpha + beta + gamma) / 2
    epsilon: float = delta
    zeta: float = delta - alpha
    eta: float = delta - beta
    theta: float = delta - gamma
    iota: float = epsilon * zeta * eta * theta
    kappa: float = sqrt(iota)
    lambda_: float = round(kappa, 2)  # lambda is a keyword, so renamed to lambda_
    return lambda_