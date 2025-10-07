from typing import Optional


def fib(integer_d: int) -> int:
    if integer_d != 0:
        if integer_d == 1:
            return 1
        else:
            temp_x: int = fib(integer_d - 1)
            temp_y: int = fib(integer_d - 2)
            return temp_x + temp_y
    return 0