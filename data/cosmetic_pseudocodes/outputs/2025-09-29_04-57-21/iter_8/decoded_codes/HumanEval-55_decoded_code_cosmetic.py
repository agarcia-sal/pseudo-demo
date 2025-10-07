from typing import Literal

def fib(number_x: int) -> int:
    match True:
        case _ if number_x == 0:
            return 0
        case _ if number_x == 1:
            return 1
    first_previous: int = fib(number_x - 1)
    second_previous: int = fib(number_x - 2)
    return first_previous + second_previous