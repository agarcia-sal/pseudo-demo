from typing import Literal

def fib(number: int) -> int:
    match number:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            firstPrev = fib(number - 1)
            secondPrev = fib(number - 2)
            return firstPrev + secondPrev