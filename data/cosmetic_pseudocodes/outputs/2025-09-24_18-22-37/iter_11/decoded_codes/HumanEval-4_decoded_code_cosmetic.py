from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        # Avoid division by zero; return 0.0 for empty input
        return 0.0

    sum_elements: float = 0.0
    idx_counter: int = 0

    while idx_counter < count_elements:
        element_value: float = list_of_numbers[idx_counter]
        sum_elements += element_value
        idx_counter += 1

    average_value: float = sum_elements / count_elements

    idx_iterator: int = 0
    sum_abs_diff: float = 0.0

    while idx_iterator < count_elements:
        current_element: float = list_of_numbers[idx_iterator]
        difference: float = current_element - average_value
        absolute_diff: float = difference if difference >= 0 else -difference
        sum_abs_diff += absolute_diff
        idx_iterator += 1

    result_value: float = sum_abs_diff / count_elements

    return result_value