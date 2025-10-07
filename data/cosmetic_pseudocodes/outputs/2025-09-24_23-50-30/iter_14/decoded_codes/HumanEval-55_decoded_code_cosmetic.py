from typing import Literal

def fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    a: int = num - 1
    b: int = num - 2
    return fib(a) + fib(b)