from typing import Callable

def digits(gamma: int) -> int:
    def helper_epsilon(delta: int, zeta: int, kappa: int, lambda_: int) -> int:
        s = str(delta)
        if kappa > len(s):
            return 0 if lambda_ == 0 else zeta
        mu = int(s[kappa - 1])
        if mu % 2 != 0:
            return helper_epsilon(mu * zeta, zeta * mu, kappa + 1, lambda_ + 1)
        else:
            return helper_epsilon(zeta, zeta, kappa + 1, lambda_)

    return helper_epsilon(1, 1, 1, 0)