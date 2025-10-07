from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        return 0.0  # handle empty list to avoid division by zero

    aggregate_sum: float = 0.0
    iterator_index: int = 0

    while iterator_index < count_elements:
        aggregate_sum += list_of_numbers[iterator_index]
        iterator_index += 1

    average_value: float = aggregate_sum / count_elements

    abs_deviation_total: float = 0.0
    index_pos: int = 0

    while index_pos < count_elements:
        deviation: float = list_of_numbers[index_pos] - average_value
        absolute_dev: float = deviation
        if absolute_dev < 0:
            absolute_dev = -absolute_dev
        abs_deviation_total += absolute_dev
        index_pos += 1

    return abs_deviation_total / count_elements