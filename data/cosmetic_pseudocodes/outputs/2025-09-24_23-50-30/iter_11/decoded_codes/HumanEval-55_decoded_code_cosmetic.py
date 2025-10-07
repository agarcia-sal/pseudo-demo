from typing import Union

def fib(delta: int) -> int:
    if delta == 0:
        return 0
    elif delta == 1:
        return 1
    else:
        alpha: int = fib(delta - 1)
        beta: int = fib(delta - 2)
        return alpha + beta