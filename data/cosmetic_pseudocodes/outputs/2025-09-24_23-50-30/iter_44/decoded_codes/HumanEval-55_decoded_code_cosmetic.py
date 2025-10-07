from typing import Literal

def fib(value_k: int) -> int:
    match value_k:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(value_k - 1) + fib(value_k - 2)