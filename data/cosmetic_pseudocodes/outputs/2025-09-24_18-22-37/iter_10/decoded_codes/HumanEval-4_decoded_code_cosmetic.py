from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        raise ValueError("list_of_numbers must not be empty")

    cumulative_sum: float = 0.0
    idx_counter: int = 0
    while idx_counter < count_elements:
        current_element: float = list_of_numbers[idx_counter]
        cumulative_sum += current_element
        idx_counter += 1

    average_value: float = cumulative_sum / count_elements

    idx_walker: int = 0
    deviation_total: float = 0.0
    while idx_walker < count_elements:
        item_value: float = list_of_numbers[idx_walker]
        difference: float = item_value - average_value
        absolute_difference: float = -difference if difference < 0 else difference
        deviation_total += absolute_difference
        idx_walker += 1

    mad_result: float = deviation_total / count_elements

    return mad_result