from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count_of_elements = len(sequence_of_values)
    if count_of_elements == 0:
        raise ValueError("sequence_of_values must not be empty")

    aggregate_sum = 0.0
    index_counter = 0
    while index_counter < count_of_elements:
        current_element = sequence_of_values[index_counter]
        aggregate_sum += current_element
        index_counter += 1
    average_indicator = aggregate_sum / count_of_elements

    cumulative_absolute_diff = 0.0
    element_cursor = 0
    while element_cursor < count_of_elements:
        single_value = sequence_of_values[element_cursor]
        intermediate_diff = single_value - average_indicator
        if intermediate_diff < 0:
            intermediate_diff = -intermediate_diff
        cumulative_absolute_diff += intermediate_diff
        element_cursor += 1

    final_result = cumulative_absolute_diff / count_of_elements
    return final_result