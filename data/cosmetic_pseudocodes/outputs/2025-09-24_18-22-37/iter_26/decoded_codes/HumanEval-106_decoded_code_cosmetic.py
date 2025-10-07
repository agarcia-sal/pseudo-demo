from typing import List

def f(beta: int) -> List[int]:
    omega: List[int] = []
    gamma: int = 1
    while gamma <= beta:
        delta: int = gamma % 2
        if delta == 0:
            epsilon = 1
            zeta = 1
            while zeta <= gamma:
                eta = epsilon
                theta = zeta
                iota = eta * theta
                epsilon = iota
                zeta += 1
            omega.append(epsilon)
        else:
            kappa = 0
            lambda_ = 1
            while lambda_ <= gamma:
                mu = kappa + lambda_
                kappa = mu
                lambda_ += 1
            omega.append(kappa)
        gamma += 1
    return omega