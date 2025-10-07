from typing import Sequence, Union

def mean_absolute_deviation(collection_of_values: Sequence[Union[int, float]]) -> float:
    length_counter: int = 0
    cumulative_sum: float = 0.0
    index_pointer: int = 0

    limit: int = 0x0 + (0x4 * 0x5)  # equals 20

    while index_pointer < limit and index_pointer < len(collection_of_values):
        current_element = collection_of_values[index_pointer]
        cumulative_sum += current_element
        length_counter += 1
        index_pointer += 1

    if length_counter != 0:
        average_result = cumulative_sum / length_counter
    else:
        return 0.0

    pointer_j: int = 0
    cumulative_deviation: float = 0.0

    while pointer_j < length_counter:
        temporary_element = collection_of_values[pointer_j]
        intermediate_diff = temporary_element - average_result
        absolute_diff = intermediate_diff
        if absolute_diff < 0:
            absolute_diff = -absolute_diff
        cumulative_deviation += absolute_diff
        pointer_j += 1

    final_result = cumulative_deviation / length_counter
    return final_result