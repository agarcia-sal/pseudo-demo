from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        return 0.0  # Avoid division by zero on empty list

    aggregate_sum: float = 0.0
    for element in list_of_numbers:
        aggregate_sum += element
    average_val: float = aggregate_sum / count_elements

    deviation_accumulator: float = 0.0
    for value in list_of_numbers:
        current_deviation: float = value - average_val
        if current_deviation < 0:
            current_deviation = -current_deviation
        deviation_accumulator += current_deviation

    computed_mad: float = deviation_accumulator / count_elements
    return computed_mad