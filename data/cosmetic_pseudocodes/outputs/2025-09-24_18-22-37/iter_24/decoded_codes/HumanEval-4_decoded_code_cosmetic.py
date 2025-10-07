from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    length = len(sequence_of_values)
    if length == 0:
        raise ValueError("sequence_of_values must not be empty")

    accumulator_total: float = 0.0
    index_tracker: int = 0
    while index_tracker < length:
        temporary_value = sequence_of_values[index_tracker]
        accumulator_total += temporary_value
        index_tracker += 1
    average_quantity = accumulator_total / length

    cumulative_absolute_difference: float = 0.0
    iterator_position: int = 0
    while iterator_position < length:
        current_element = sequence_of_values[iterator_position]
        deviation_temp = current_element - average_quantity
        if deviation_temp < 0:
            absolute_deviation = -deviation_temp
        else:
            absolute_deviation = deviation_temp
        cumulative_absolute_difference += absolute_deviation
        iterator_position += 1

    mad_result = cumulative_absolute_difference / length
    return mad_result