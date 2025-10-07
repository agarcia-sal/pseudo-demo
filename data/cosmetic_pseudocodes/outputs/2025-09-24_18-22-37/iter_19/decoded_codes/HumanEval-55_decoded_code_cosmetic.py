from typing import Union

def fib(index_x: int) -> int:
    # Base cases for Fibonacci sequence
    if index_x == 0:
        return 0
    if index_x == 1:
        return 1
    delta_y = index_x - 1
    delta_z = index_x - 2
    val_p = fib(delta_y)
    val_q = fib(delta_z)
    val_r = val_p + val_q
    return val_r