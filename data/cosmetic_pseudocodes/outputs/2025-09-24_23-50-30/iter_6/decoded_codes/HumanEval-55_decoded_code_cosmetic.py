from typing import Union

def fib(alpha: int) -> int:
    if alpha == 0:
        return 0
    elif alpha == 1:
        return 1
    else:
        beta: int = alpha - 1
        gamma: int = alpha - 2
        delta: int = fib(beta)
        epsilon: int = fib(gamma)
        return delta + epsilon