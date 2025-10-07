from typing import Literal


def fib(delta: int) -> int:
    match delta:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(delta - 1) + fib(delta - 2)