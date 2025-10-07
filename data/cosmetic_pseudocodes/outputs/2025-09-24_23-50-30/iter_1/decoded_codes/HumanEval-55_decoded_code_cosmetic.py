from typing import Literal


def fib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    elif integer_n == 1:
        return 1
    else:
        a: int = fib(integer_n - 1)
        b: int = fib(integer_n - 2)
        return a + b