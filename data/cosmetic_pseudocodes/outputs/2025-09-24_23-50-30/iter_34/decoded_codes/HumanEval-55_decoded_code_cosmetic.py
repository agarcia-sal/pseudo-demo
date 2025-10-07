from typing import Literal

def fib(alpha: int) -> int:
    if alpha == 0:
        return 0
    elif alpha == 1:
        return 1
    else:
        beta = alpha - 1
        gamma = alpha - 2
        return fib(beta) + fib(gamma)