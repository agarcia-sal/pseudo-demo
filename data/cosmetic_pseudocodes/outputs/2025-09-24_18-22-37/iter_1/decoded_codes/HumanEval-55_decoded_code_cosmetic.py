from typing import Literal

def fib(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            a = fib(n - 1)
            b = fib(n - 2)
            return a + b