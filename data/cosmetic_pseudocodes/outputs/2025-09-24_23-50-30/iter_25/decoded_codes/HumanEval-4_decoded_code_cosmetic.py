from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count: int = len(sequence_of_values)
    if count == 0:
        raise ValueError("sequence_of_values must not be empty")

    cumulative_sum: float = 0.0
    for index in range(count):
        cumulative_sum += sequence_of_values[index]

    average: float = cumulative_sum / count

    sum_deviation: float = 0.0
    position: int = 0
    while position < count:
        deviation: float = sequence_of_values[position] - average
        if deviation < 0:
            deviation = -deviation
        sum_deviation += deviation
        position += 1

    final_result: float = sum_deviation / count
    return final_result