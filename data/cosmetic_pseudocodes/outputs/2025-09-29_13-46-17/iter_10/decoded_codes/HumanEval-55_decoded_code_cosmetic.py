from typing import Callable

def fib(integer_n: int) -> int:
    def fib_inner(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib_inner(n - 1) + fib_inner(n - 2)
    return fib_inner(integer_n)