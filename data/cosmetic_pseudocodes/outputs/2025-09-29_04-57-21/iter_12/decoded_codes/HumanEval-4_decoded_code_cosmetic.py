from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    aggregate_sum: float = 0.0
    index_tracker: int = 0
    while index_tracker < count_elements:
        aggregate_sum += list_of_numbers[index_tracker]
        index_tracker += 1
    average: float = aggregate_sum / count_elements

    deviation_accumulator: float = 0.0
    iterator_position: int = 0
    while iterator_position < count_elements:
        deviation_accumulator += abs(list_of_numbers[iterator_position] - average)
        iterator_position += 1

    result_mad: float = deviation_accumulator / count_elements
    return result_mad