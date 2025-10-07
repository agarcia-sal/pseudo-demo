from typing import Literal

def fib(parameter_k: int) -> int:
    match parameter_k:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(parameter_k - 1) + fib(parameter_k - 2)