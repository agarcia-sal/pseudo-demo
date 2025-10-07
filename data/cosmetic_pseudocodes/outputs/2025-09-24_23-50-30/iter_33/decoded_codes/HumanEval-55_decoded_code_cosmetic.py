from typing import Literal


def fib(alpha: int) -> int:
    if alpha == 0:
        return 0
    elif alpha == 1:
        return 1
    else:
        delta: int = alpha - 1
        epsilon: int = alpha - 2
        return fib(delta) + fib(epsilon)