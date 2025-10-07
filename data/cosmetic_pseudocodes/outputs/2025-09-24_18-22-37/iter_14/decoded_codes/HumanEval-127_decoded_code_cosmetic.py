from typing import Sequence

def intersection(alpha: Sequence[int], beta: Sequence[int]) -> str:
    def is_prime(gamma: int) -> bool:
        if gamma == 0 or gamma == 1:
            return False
        if gamma == 2:
            return True
        for epsilon in range(2, gamma):
            if gamma % epsilon == 0:
                return False
        return True

    theta = alpha[0]
    iota = beta[0]
    kappa = theta if theta > iota else iota

    lambda_ = alpha[1]  # lambda is a reserved word in Python
    mu = beta[1]
    nu = lambda_ if lambda_ < mu else mu

    xi = nu - kappa
    if xi > 0 and is_prime(xi):
        return "YES"
    return "NO"