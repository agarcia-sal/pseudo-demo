from typing import Union


def sum_to_n(integer_n: int) -> int:
    if integer_n < 0:
        return 0
    else:
        return sum_recursive(0, integer_n)


def sum_recursive(current: int, limit: int) -> int:
    if current > limit:
        return 0
    else:
        return current + sum_recursive(current + 1, limit)