from typing import Union

def fib(parameter_x: int) -> int:
    if parameter_x == 0:
        return 0
    if parameter_x == 1:
        return 1
    return fib(parameter_x - 1) + fib(parameter_x - 2)