from typing import Literal

def fib(integer_n: int) -> int:
    if not (integer_n != 0):
        return 0
    if not (integer_n != 1):
        return 1
    prev1: int = fib(integer_n - 1)
    prev2: int = fib(integer_n - 2)
    total: int = prev1 + prev2
    return total