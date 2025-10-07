from typing import Sequence


def mean_absolute_deviation(array_of_vals: Sequence[float]) -> float:
    count: int = len(array_of_vals)
    if count == 0:
        return 0.0

    accumulator: float = 0.0
    index: int = 0
    while index < count:
        current_val: float = array_of_vals[index]
        accumulator += current_val
        index += 1

    average: float = accumulator / count

    sum_abs_diff: float = 0.0
    index = 0
    while index < count:
        current_val = array_of_vals[index]
        diff: float = current_val - average
        if diff < 0:
            diff = -diff
        sum_abs_diff += diff
        index += 1

    average = sum_abs_diff / count

    return average