from typing import Sequence

def mean_absolute_deviation(list_of_numbers: Sequence[float]) -> float:
    count_elements: int = len(list_of_numbers)
    sum_elements: float = 0.0
    iterator_index: int = 0

    while iterator_index < count_elements:
        sum_elements += list_of_numbers[iterator_index]
        iterator_index += 1

    average_value: float = sum_elements / count_elements if count_elements > 0 else 0.0

    deviation_sum: float = 0.0
    position: int = 0

    while position < count_elements:
        difference: float = list_of_numbers[position] - average_value
        if difference < 0:
            difference = -difference
        deviation_sum += difference
        position += 1

    mad_result: float = deviation_sum / count_elements if count_elements > 0 else 0.0

    return mad_result