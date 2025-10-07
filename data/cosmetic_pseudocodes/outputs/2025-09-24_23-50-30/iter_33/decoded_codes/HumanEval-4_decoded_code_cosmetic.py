from typing import Sequence

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    count: int = len(sequence)
    if count == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    accumulator: float = 0.0
    for index in range(count):
        accumulator += sequence[index]
    average: float = accumulator / count

    deviations: list[float] = []
    pointer: int = 0
    while pointer < count:
        deviation: float = sequence[pointer] - average
        absolute_deviation: float = deviation if deviation >= 0 else -deviation
        deviations.append(absolute_deviation)
        pointer += 1

    sum_absolute_deviation: float = 0.0
    for element in deviations:
        sum_absolute_deviation += element

    return sum_absolute_deviation / count