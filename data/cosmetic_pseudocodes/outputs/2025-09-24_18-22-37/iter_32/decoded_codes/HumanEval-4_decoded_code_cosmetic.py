from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        return 0.0  # handle empty list edge case gracefully
    accumulator_mean: float = 0.0
    index_counter: int = 0
    while index_counter < count_elements:
        accumulator_mean += list_of_numbers[index_counter]
        index_counter += 1
    average_value: float = accumulator_mean / count_elements

    sum_absolute_diff: float = 0.0
    cursor: int = 0
    while cursor < count_elements:
        current_element = list_of_numbers[cursor]
        difference = current_element - average_value
        if difference < 0:
            difference = -difference
        sum_absolute_diff += difference
        cursor += 1

    mad_result: float = sum_absolute_diff / count_elements

    return mad_result