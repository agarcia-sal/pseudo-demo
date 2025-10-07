from typing import Sequence

def mean_absolute_deviation(numbers_array: Sequence[float]) -> float:
    deviation_accumulator: float = 0.0
    count_elements: int = len(numbers_array)
    summation: float = 0.0

    for index in range(count_elements):
        summation += numbers_array[index]

    average_value: float = summation * (1 / count_elements)

    index_counter: int = 0
    while index_counter < count_elements:
        if average_value > numbers_array[index_counter]:
            deviation_accumulator += average_value - numbers_array[index_counter]
        else:
            deviation_accumulator += numbers_array[index_counter] - average_value
        index_counter += 1

    result_value: float = deviation_accumulator * (1 / count_elements)

    return result_value