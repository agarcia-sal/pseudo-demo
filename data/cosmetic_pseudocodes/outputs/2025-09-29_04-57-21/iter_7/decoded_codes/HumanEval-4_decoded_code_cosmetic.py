from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count_elements: int = len(sequence_of_values)
    aggregate_sum: float = 0.0
    index_counter: int = 0

    while index_counter < count_elements:
        aggregate_sum += sequence_of_values[index_counter]
        index_counter += 1

    average: float = aggregate_sum / count_elements

    accumulated_deviation: float = 0.0
    position_tracker: int = 0

    while position_tracker < count_elements:
        deviation: float = sequence_of_values[position_tracker] - average
        if not (deviation < 0):
            absolute_deviation: float = deviation
        else:
            absolute_deviation = -deviation
        accumulated_deviation += absolute_deviation
        position_tracker += 1

    result_mad: float = accumulated_deviation / count_elements

    return result_mad