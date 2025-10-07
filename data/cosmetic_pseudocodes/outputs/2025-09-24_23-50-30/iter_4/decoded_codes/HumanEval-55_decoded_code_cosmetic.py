from typing import Literal

def fib(n: int) -> int:
    return (n == 0) * 0 + (n == 1) * 1 + ((n > 1) * (fib(n - 1) + fib(n - 2)))