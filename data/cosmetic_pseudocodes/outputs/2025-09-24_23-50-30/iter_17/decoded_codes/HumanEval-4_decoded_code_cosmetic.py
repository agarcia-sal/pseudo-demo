from typing import Sequence

def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    count_of_elements: int = len(array_of_values)
    if count_of_elements == 0:
        raise ValueError("array_of_values must not be empty")
    sum_of_elements: float = 0.0
    index_counter: int = 0
    while index_counter < count_of_elements:
        sum_of_elements += array_of_values[index_counter]
        index_counter += 1
    average_value: float = sum_of_elements / count_of_elements

    absolute_differences: list[float] = []
    walker: int = 0
    while True:
        if walker == count_of_elements:
            break
        distance: float = array_of_values[walker] - average_value
        magnitude: float = distance if distance >= 0 else -distance
        absolute_differences.append(magnitude)
        walker += 1

    accumulated_deviation: float = 0.0
    for number in absolute_differences:
        accumulated_deviation += number

    result_value: float = accumulated_deviation / count_of_elements
    return result_value