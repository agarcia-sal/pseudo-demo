from math import sqrt
from typing import Union


def triangle_area(zeta: float, xi: float, omega: float) -> float:
    # Check if any side inequality prevents a valid triangle
    if (zeta + xi) <= omega or (zeta + omega) <= xi or (xi + omega) <= zeta:
        return -1.0
    gamma: float = (zeta + xi + omega) / 2
    alpha: float = gamma * (gamma - zeta)
    kappa: float = gamma - xi
    lambda_: float = gamma - omega
    mu: float = alpha * kappa
    nu: float = mu * lambda_
    sigma: float = sqrt(nu)
    rho: float = round(sigma, 2)
    return rho