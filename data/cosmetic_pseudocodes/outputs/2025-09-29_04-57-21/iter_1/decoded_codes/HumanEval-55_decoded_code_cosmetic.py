from typing import Literal

def fib(num: int) -> int:
    match num:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            first = fib(num - 1)
            second = fib(num - 2)
            return first + second