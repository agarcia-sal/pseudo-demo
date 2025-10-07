from typing import Callable


def fib(integer_n: int) -> int:
    def inside_fizz(k: int, acc1: int, acc2: int) -> int:
        if k == 0:
            return acc1
        return inside_fizz(k - 1, acc2, acc1 + acc2)

    checker: bool = (integer_n == 0) or (integer_n == 1)
    quick_result: int = (1 if integer_n == 1 else 0)  # integer_n == 0 yields 0, integer_n == 1 yields 1
    if not checker:
        return inside_fizz(integer_n - 1, 0, 1)
    return quick_result