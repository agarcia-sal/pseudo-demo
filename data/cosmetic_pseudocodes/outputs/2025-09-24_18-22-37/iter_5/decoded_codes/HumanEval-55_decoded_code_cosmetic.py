from typing import Union


def fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    first_predecessor: int = fib(num - 1)
    second_predecessor: int = fib(num - 2)
    result_sum: int = first_predecessor + second_predecessor
    return result_sum