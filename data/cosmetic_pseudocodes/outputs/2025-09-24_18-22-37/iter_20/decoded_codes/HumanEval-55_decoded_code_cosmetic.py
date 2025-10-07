from typing import Literal

def fib(alpha: int) -> int:
    if alpha == 0:
        return 0
    if alpha == 1:
        return 1
    delta1 = alpha - 1
    delta2 = alpha - 2
    theta = fib(delta1)
    omega = fib(delta2)
    sigma = theta + omega
    return sigma