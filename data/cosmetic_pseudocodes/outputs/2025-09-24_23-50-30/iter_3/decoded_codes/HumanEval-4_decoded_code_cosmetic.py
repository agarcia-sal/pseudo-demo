from functools import reduce
from typing import Sequence

def mean_absolute_deviation(numbers: Sequence[float]) -> float:
    n: int = len(numbers)
    if n == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    avg: float = reduce(lambda acc, x: acc + x, numbers, 0) / n
    sum_dev: float = 0
    for index in range(n):
        diff: float = numbers[index] - avg
        if diff < 0:
            diff = -diff
        sum_dev += diff
    return sum_dev / n