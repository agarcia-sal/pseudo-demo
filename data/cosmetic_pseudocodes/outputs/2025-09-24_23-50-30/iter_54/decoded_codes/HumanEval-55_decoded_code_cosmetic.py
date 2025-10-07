from typing import Literal

def fib(param_n: int) -> int:
    match param_n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            arg_a: int = param_n - 1
            arg_b: int = param_n - 2
            return fib(arg_a) + fib(arg_b)