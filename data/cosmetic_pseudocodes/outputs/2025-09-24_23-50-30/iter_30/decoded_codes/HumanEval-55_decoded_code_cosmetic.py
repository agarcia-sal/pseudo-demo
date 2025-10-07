from typing import Literal

def fib(delta: int) -> int:
    if delta == 0:
        return 0
    elif delta == 1:
        return 1
    else:
        xi = delta - 1
        yi = delta - 2
        return fib(xi) + fib(yi)