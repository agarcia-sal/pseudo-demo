from typing import Sequence

def mean_absolute_deviation(numbers_sequence: Sequence[float]) -> float:
    count: int = len(numbers_sequence)
    if count == 0:
        raise ValueError("numbers_sequence must not be empty")
    aggregate: float = 0.0
    for index in range(count):
        aggregate += numbers_sequence[index]
    average: float = aggregate / count

    deviation_sum: float = 0.0
    for element in numbers_sequence:
        difference: float = element - average
        if difference < 0:
            difference = -difference
        deviation_sum += difference

    result: float = deviation_sum / count
    return result