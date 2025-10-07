from typing import Callable

def special_factorial(count_target: int) -> int:
    repeat_index: int = 1
    accumulated_product: int = 1
    cumulative_factorial: int = 1
    while repeat_index <= count_target:
        accumulated_product *= repeat_index
        cumulative_factorial *= accumulated_product
        repeat_index += 1
    return cumulative_factorial