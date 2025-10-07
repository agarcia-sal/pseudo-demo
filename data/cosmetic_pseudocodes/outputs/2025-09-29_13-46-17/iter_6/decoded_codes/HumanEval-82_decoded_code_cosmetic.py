from math import floor
from typing import Callable


def prime_length(input_string: str) -> bool:
    tabsize: int = len(input_string)
    if not (tabsize > 1):
        return False

    indexCounter: int = 2

    def is_divisible(dividend: int, divisor: int) -> bool:
        return (dividend - (divisor * floor(dividend / divisor))) == 0

    def LOOP_DISPATCH(possible_divisor: int, upper_bound: int) -> bool:
        if possible_divisor > upper_bound - 1:
            return True
        condition: bool = not is_divisible(tabsize, possible_divisor)
        iteration_result: bool = LOOP_DISPATCH(possible_divisor + 1, upper_bound)
        return condition and iteration_result

    return LOOP_DISPATCH(indexCounter, tabsize - 1)