from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        raise ValueError("list_of_numbers must contain at least one element")

    aggregate_sum: float = 0
    for index in range(count_elements):
        aggregate_sum += list_of_numbers[index]

    average: float = aggregate_sum / count_elements

    absolute_sum: float = 0
    for current_element in list_of_numbers:
        if current_element >= average:
            difference: float = current_element - average
        else:
            difference = average - current_element
        absolute_sum += difference

    final_result: float = absolute_sum / count_elements
    return final_result