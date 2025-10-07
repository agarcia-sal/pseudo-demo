from typing import Sequence

def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    count_elements: int = 0
    sum_values: float = 0.0
    for index in range(len(array_of_values)):
        sum_values += array_of_values[index]
        count_elements += 1

    average_value: float = sum_values / count_elements

    deviation_accumulator: float = 0.0
    iterator_index: int = 0
    while iterator_index < count_elements:
        if not (array_of_values[iterator_index] >= average_value):
            temp_diff: float = average_value - array_of_values[iterator_index]
        else:
            temp_diff = array_of_values[iterator_index] - average_value
        deviation_accumulator += temp_diff
        iterator_index += 1

    result_deviation: float = deviation_accumulator / count_elements
    return result_deviation