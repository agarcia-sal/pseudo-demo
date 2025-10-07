from math import sqrt
from typing import Union


def triangle_area(lambda_: float, mu: float, nu: float) -> float:
    # Check triangle inequality
    if not ((lambda_ + mu > nu) and (lambda_ + nu > mu) and (mu + nu > lambda_)):
        return -1.0
    rho: float = 0.5 * (nu + mu + lambda_)
    sigma: float = sqrt(rho * (rho - lambda_) * (rho - mu) * (rho - nu))
    tau: float = round(sigma * 100) / 100
    return tau