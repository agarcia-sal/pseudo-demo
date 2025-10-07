from typing import Union


def fib(p: int) -> int:
    if p == 0:
        return 0
    elif p == 1:
        return 1
    else:
        a: int = p - 1
        b: int = p - 2
        x: int = fib(a)
        y: int = fib(b)
        z: int = x + y
        return z