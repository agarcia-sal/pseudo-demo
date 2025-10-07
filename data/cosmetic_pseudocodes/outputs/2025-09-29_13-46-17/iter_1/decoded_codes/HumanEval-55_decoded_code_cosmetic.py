from typing import Literal

def fib(integer_n: int) -> int:
    match integer_n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            first_previous = fib(integer_n - 1)
            second_previous = fib(integer_n - 2)
            return first_previous + second_previous