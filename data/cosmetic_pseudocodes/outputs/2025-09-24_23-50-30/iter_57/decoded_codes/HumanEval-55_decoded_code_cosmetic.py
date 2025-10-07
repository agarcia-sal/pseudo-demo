from typing import Literal

def fib(numb_x: int) -> int:
    if numb_x == 0:
        return 0
    elif numb_x == 1:
        return 1
    else:
        index_y = numb_x - 1
        index_z = numb_x - 2
        return fib(index_y) + fib(index_z)