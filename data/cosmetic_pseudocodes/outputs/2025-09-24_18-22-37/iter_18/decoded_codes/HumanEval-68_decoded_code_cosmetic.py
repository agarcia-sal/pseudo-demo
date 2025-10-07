from typing import List


def pluck(gamma: List[int]) -> List[int]:
    delta: List[int] = []
    if not (len(gamma) > 0):
        return delta

    epsilon: List[int] = []
    zeta: int = 0

    while zeta < len(gamma):
        eta: int = gamma[zeta]
        if (eta % 2) == 0:
            epsilon.append(eta)
        zeta += 1

    if not (len(epsilon) > 0):
        return delta

    theta: int = epsilon[0]
    iota: int = 0
    kappa: int = 1

    while kappa < len(epsilon):
        if epsilon[kappa] < theta:
            theta = epsilon[kappa]
            iota = kappa
        kappa += 1

    lambda_: int = 0
    mu: int = 0
    while lambda_ < len(gamma):
        if gamma[lambda_] == theta:
            mu = lambda_
            break
        lambda_ += 1

    return [theta, mu]