from math import sqrt

def triangle_area(beta: float, gamma: float, alpha: float) -> float:
    if not (beta + gamma > alpha and beta + alpha > gamma and alpha + gamma > beta):
        return -1.0
    delta = (beta + gamma + alpha) / 2
    epsilon = sqrt(delta * (delta - beta) * (delta - gamma) * (delta - alpha))
    zeta = round(epsilon, 2)
    return zeta