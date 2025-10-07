from typing import Any


def fib(integer_n: int) -> int:
    if integer_n != 0:
        if integer_n != 1:
            return fib(integer_n - 1) + fib(integer_n - 2)
        return 1
    return 0