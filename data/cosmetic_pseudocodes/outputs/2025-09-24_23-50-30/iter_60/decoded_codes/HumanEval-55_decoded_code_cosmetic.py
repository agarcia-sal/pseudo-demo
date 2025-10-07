from typing import Literal

def fib(alpha: int) -> int:
    match alpha:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(alpha - 1) + fib(alpha - 2)