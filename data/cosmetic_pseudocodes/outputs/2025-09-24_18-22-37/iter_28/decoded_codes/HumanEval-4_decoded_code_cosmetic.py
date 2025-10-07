from typing import Sequence

def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    count_elements: int = len(array_of_values)
    if count_elements == 0:
        raise ValueError("array_of_values must not be empty")

    sum_values: float = 0.0
    index_tracker: int = 0
    while index_tracker < count_elements:
        temp_val: float = array_of_values[index_tracker]
        sum_values += temp_val
        index_tracker += 1

    average_value: float = sum_values / count_elements
    abs_dev_total: float = 0.0
    pos_iterator: int = 0

    while pos_iterator < count_elements:
        current_element: float = array_of_values[pos_iterator]
        difference: float = current_element - average_value
        abs_diff: float = -difference if difference < 0 else difference
        abs_dev_total += abs_diff
        pos_iterator += 1

    final_result: float = abs_dev_total / count_elements
    return final_result