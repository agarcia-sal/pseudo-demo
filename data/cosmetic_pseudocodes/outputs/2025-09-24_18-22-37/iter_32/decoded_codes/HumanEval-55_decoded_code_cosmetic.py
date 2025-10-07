from typing import Optional


def fib(integer_n: int) -> int:
    if integer_n == 0:
        several_ax: int = 0
    elif integer_n == 1:
        several_ax = 1
    else:
        lh: int = fib(integer_n - 1)
        rk: int = fib(integer_n - 2)
        several_ax = lh + rk
    return several_ax