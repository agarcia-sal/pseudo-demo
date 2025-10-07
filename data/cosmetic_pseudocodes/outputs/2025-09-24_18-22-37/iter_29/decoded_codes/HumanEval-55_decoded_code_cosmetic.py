from typing import Literal

def fib(mInteger: int) -> int:
    match mInteger:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            a = mInteger - 1
            b = mInteger - 2
            x = fib(a)
            y = fib(b)
            return x + y