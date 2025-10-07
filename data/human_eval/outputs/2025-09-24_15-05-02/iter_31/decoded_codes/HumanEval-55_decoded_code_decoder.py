from functools import cache

def fib(integer_n: int) -> int:
    if integer_n < 0:
        raise ValueError("Input must be a non-negative integer")

    @cache
    def _fib(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return _fib(n - 1) + _fib(n - 2)

    return _fib(integer_n)