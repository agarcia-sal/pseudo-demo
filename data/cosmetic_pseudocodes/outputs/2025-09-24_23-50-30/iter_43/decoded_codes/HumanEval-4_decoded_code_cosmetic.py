from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count: int = len(sequence_of_values)
    if count == 0:
        return 0.0  # Avoid division by zero, return 0 for empty input

    accumulator: float = 0.0
    for index in range(count):
        accumulator += sequence_of_values[index]
    average: float = accumulator / count

    deviation_sum: float = 0.0
    for idx in range(count):
        deviation: float = sequence_of_values[idx] - average
        if deviation < 0:
            deviation = -deviation
        deviation_sum += deviation

    return deviation_sum / count