from typing import Sequence

def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    count: int = 0
    aggregate_sum: float = 0.0
    index: int = 0
    length: int = len(numbers_collection)
    while index < length:
        aggregate_sum += numbers_collection[index]
        count += 1
        index += 1
    average: float = aggregate_sum / count

    index = 0
    sum_deviation: float = 0.0
    while index < count:
        deviation: float = numbers_collection[index] - average
        if deviation < 0:
            deviation = -deviation
        sum_deviation += deviation
        index += 1
    mean_abs_dev: float = sum_deviation / count
    return mean_abs_dev