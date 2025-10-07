from typing import Callable


def sum_to_n(integer_n: int) -> int:
    return helper_sum(0, integer_n, 0)


def helper_sum(current_value: int, maximum_value: int, accumulated_total: int) -> int:
    if current_value > maximum_value:
        return accumulated_total
    else:
        return helper_sum(current_value + 1, maximum_value, accumulated_total + current_value)