from typing import Callable

def add(x: int, y: int) -> int:
    def accumulate(lambda_: int, mu: int, nu: int) -> int:
        if nu == 0:
            return mu
        else:
            return accumulate(lambda_, mu + 1, nu - 1)
    rho = accumulate(x, y, 0)
    return rho