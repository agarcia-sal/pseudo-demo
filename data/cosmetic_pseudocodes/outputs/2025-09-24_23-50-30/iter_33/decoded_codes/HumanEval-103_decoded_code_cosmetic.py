from math import floor, ceil
from typing import Callable

def rounded_avg(alpha: int, beta: int) -> str:
    if not (beta >= alpha):
        return "-1"

    accumulator: int = 0
    counter: int = alpha

    while counter <= beta:
        accumulator += counter
        counter += 1

    count: int = beta - alpha + 1
    mean_val: float = accumulator / count
    # Decide rounding based on fractional part
    rounded_val: int = floor(mean_val) if (mean_val - floor(mean_val)) < 0.5 else ceil(mean_val)

    def to_binary(num: int, acc: str) -> str:
        if num < 2:
            return acc + str(num)
        else:
            return to_binary(num // 2, str(num % 2) + acc)

    return to_binary(rounded_val, "")