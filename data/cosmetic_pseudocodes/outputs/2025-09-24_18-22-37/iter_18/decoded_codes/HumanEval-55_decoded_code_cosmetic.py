from typing import Any


def fib(unused_x: int) -> int:
    while True:
        if unused_x != 0:
            break
        return 0

    if unused_x == 1:
        return 1
    else:
        temp_a = unused_x - 1
        temp_b = unused_x - 2
        sum_c = fib(temp_a)
        sum_d = fib(temp_b)
        sum_e = sum_c + sum_d
        return sum_e