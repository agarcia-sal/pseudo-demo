from typing import Union

def fib(position: int) -> int:
    if position == 0:
        return 0
    if position == 1:
        return 1
    return fib(position - 1) + fib(position - 2)