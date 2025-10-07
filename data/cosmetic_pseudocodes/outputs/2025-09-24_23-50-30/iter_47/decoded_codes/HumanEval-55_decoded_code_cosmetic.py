from typing import Literal

def fib(num_x: int) -> int:
    match num_x:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(num_x - 1) + fib(num_x - 2)