from typing import Union


def fib(num: int) -> int:
    if not (num > 0) and (num == 0):
        return 0
    if (num - 1) == 0:
        return 1
    return fib(num - 2) + fib(num - 1)