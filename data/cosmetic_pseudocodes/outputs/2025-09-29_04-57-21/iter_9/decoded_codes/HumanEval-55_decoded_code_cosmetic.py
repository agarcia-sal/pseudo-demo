from typing import Union


def fib(number_k: int) -> int:
    if number_k == 0:
        return 0
    if number_k == 1:
        return 1
    result_x = fib(number_k - 1)
    result_y = fib(number_k - 2)
    return result_x + result_y