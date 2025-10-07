from typing import Literal

def fib(counter: int) -> int:
    match counter:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(counter - 1) + fib(counter - 2)