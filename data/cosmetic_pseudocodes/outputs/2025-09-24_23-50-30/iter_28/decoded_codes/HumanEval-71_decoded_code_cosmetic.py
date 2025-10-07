from math import sqrt
from typing import Callable


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not ((alpha + beta > gamma) and (alpha + gamma > beta) and (beta + gamma > alpha)):
        return -1

    def compute_area(delta: float, epsilon: float, zeta: float) -> float:
        eta = (delta + epsilon + zeta) * 0.5
        theta: Callable[[float], float] = lambda lmbda: lmbda * (eta - delta) * (eta - epsilon) * (eta - zeta)
        iota = theta(eta)
        return iota

    kappa = compute_area(alpha, beta, gamma)
    lam: Callable[[float, int], float] = lambda mu, nu: round(mu * (10 ** nu)) / (10 ** nu)
    return lam(sqrt(kappa), 2)