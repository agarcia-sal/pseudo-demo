from typing import Union

def fib(delta_x: int) -> int:
    if delta_x == 0:
        return 0
    if delta_x == 1:
        return 1
    left_argument = delta_x - 1
    right_argument = delta_x - 2
    left_result = fib(left_argument)
    right_result = fib(right_argument)
    cumulative_result = left_result + right_result
    return cumulative_result