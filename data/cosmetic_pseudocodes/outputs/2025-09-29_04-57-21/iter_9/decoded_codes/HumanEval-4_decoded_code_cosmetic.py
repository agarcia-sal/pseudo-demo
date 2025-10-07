from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_numbers: int = len(list_of_numbers)
    sum_numbers: float = 0.0
    index_counter: int = 0
    while index_counter < count_numbers:
        sum_numbers += list_of_numbers[index_counter]
        index_counter += 1
    average_value: float = sum_numbers / count_numbers

    accumulated_deviation: float = 0.0
    iterator_position: int = 0
    while iterator_position < count_numbers:
        deviation_element: float = list_of_numbers[iterator_position]
        absolute_diff: float = deviation_element - average_value
        if absolute_diff < 0:
            absolute_diff = -absolute_diff
        accumulated_deviation += absolute_diff
        iterator_position += 1

    final_result: float = accumulated_deviation / count_numbers
    return final_result