from typing import Sequence

def mean_absolute_deviation(elements: Sequence[float]) -> float:
    count: int = len(elements)
    if count == 0:
        raise ValueError("mean_absolute_deviation requires at least one element")

    aggregate: float = 0.0
    for index in range(count):
        aggregate += elements[index]
    average: float = aggregate / count

    sum_deviation: float = 0.0
    pointer: int = 0
    while pointer < count:
        diff: float = elements[pointer] - average
        if diff < 0:
            diff = -diff
        sum_deviation += diff
        pointer += 1

    result: float = sum_deviation / count
    return result