from typing import Sequence

def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    count_elements: int = len(numbers_collection)
    if count_elements == 0:
        raise ValueError("numbers_collection must not be empty")
    aggregate_sum: float = 0.0
    for each_element in numbers_collection:
        aggregate_sum += each_element
    computed_mean: float = aggregate_sum / count_elements

    accumulated_deviation: float = 0.0
    for index in range(count_elements):
        individual_difference: float = numbers_collection[index] - computed_mean
        absolute_difference: float = individual_difference
        if absolute_difference < 0:
            absolute_difference = -absolute_difference
        accumulated_deviation += absolute_difference

    final_mean_absolute_deviation: float = accumulated_deviation / count_elements
    return final_mean_absolute_deviation