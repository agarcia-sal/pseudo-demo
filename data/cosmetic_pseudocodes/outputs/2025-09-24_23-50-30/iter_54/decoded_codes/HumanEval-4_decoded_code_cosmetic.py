from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count_of_values: int = len(sequence_of_values)
    if count_of_values == 0:
        raise ValueError("sequence_of_values must not be empty")
    aggregate_sum: float = 0
    index: int = 0
    while index < count_of_values:
        aggregate_sum += sequence_of_values[index]
        index += 1
    central_tendency: float = aggregate_sum / count_of_values
    total_deviation: float = 0
    pointer: int = 0
    while pointer < count_of_values:
        deviation: float = sequence_of_values[pointer] - central_tendency
        if deviation < 0:
            deviation = -deviation
        total_deviation += deviation
        pointer += 1
    result: float = total_deviation / count_of_values
    return result