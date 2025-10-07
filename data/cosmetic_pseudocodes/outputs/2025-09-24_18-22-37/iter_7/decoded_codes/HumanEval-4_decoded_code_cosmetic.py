from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count: int = len(sequence_of_values)
    if count == 0:
        raise ValueError("sequence_of_values must not be empty")

    sum_values: float = 0.0
    index: int = 0
    while index < count:
        sum_values += sequence_of_values[index]
        index += 1

    average: float = sum_values / count

    sum_abs_diff: float = 0.0
    position: int = 0
    while position < count:
        difference: float = sequence_of_values[position] - average
        absolute_diff: float = -difference if difference < 0 else difference
        sum_abs_diff += absolute_diff
        position += 1

    result: float = sum_abs_diff / count
    return result