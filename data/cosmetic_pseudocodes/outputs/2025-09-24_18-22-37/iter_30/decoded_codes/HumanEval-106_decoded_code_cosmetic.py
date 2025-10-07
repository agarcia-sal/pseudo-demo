from typing import List


def f(alpha: int) -> List[int]:
    omega: List[int] = []
    delta: int = 1
    sigma: int = 0
    zeta: int = 0
    kappa: int = 1
    theta: int = 1

    while kappa <= alpha:
        beta: int = kappa % 2
        if beta == 0:
            delta = 1
            zeta = 1
            while zeta <= kappa:
                delta *= zeta
                zeta += 1
            omega.append(delta)
        else:  # beta == 1
            sigma = 0
            theta = 1
            while theta <= kappa:
                sigma += theta
                theta += 1
            omega.append(sigma)
        kappa += 1

    return omega