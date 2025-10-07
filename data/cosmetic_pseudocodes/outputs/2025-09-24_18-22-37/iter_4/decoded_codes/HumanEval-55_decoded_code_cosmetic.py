from typing import Literal

def fib(num: int) -> int:
    match num:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            a = num - 1
            b = num - 2
            return fib(a) + fib(b)