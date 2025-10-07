from typing import Literal

def fib(num: int) -> int:
    match num:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(num - 1) + fib(num - 2)