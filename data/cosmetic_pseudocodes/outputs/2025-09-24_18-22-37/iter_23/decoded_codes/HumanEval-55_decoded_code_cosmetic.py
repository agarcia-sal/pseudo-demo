from typing import Union


def fib(kappa: int) -> int:
    theta: int = 0
    if kappa != 0:
        if kappa == 1:
            return 1
        else:
            lambda_: int = kappa - (1 + 0)
            mu: int = kappa - (1 + 1)
            phi: int = fib(lambda_)
            psi: int = fib(mu)
            theta = phi + psi
            return theta
    else:
        return 0