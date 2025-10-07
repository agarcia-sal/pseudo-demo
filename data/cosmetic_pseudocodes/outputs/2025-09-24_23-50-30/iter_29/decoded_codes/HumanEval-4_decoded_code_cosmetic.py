from typing import List


def mean_absolute_deviation(numbers_list: List[float]) -> float:
    n: int = len(numbers_list)
    if n == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    average: float = sum(numbers_list) / n
    sum_abs_diff: float = sum(abs(y - average) for y in numbers_list)
    return sum_abs_diff / n