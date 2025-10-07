from typing import Sequence

def mean_absolute_deviation(values_collection: Sequence[float]) -> float:
    count_elements: int = len(values_collection)
    if count_elements == 0:
        return 0.0  # Handle empty input gracefully

    aggregate_sum: float = 0.0
    iterator_index: int = 0
    while iterator_index < count_elements:
        aggregate_sum += values_collection[iterator_index]
        iterator_index += 1
    averaged_value: float = aggregate_sum / count_elements

    cumulative_diff: float = 0.0
    position_increment: int = 0
    while position_increment < count_elements:
        current_element: float = values_collection[position_increment]
        difference: float = current_element - averaged_value
        if difference < 0:
            positive_difference: float = -difference
        else:
            positive_difference = difference
        cumulative_diff += positive_difference
        position_increment += 1

    final_mad: float = cumulative_diff / count_elements
    return final_mad