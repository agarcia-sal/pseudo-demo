from typing import Literal

def fib(integer_n: int) -> int:
    match integer_n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            result1: int = fib(integer_n - 2)
            result2: int = fib(integer_n - 1)
            return result2 + result1