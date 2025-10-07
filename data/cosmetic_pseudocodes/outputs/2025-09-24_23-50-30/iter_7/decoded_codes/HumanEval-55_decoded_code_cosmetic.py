from functools import cache

@cache
def fib(alpha: int) -> int:
    if alpha == 0:
        return 0
    if alpha == 1:
        return 1
    return fib(alpha - 1) + fib(alpha - 2)