from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count_of_elements: int = len(sequence_of_values)
    if count_of_elements == 0:
        raise ValueError("mean_absolute_deviation requires at least one value")
    total_sum: float = 0.0
    for index in range(count_of_elements):
        total_sum += sequence_of_values[index]
    average: float = total_sum / count_of_elements

    deviation_accumulator: float = 0.0
    current_position: int = 0
    while current_position < count_of_elements:
        current_element: float = sequence_of_values[current_position]
        if current_element >= average:
            deviation_accumulator += current_element - average
        else:
            deviation_accumulator += average - current_element
        current_position += 1

    final_result: float = deviation_accumulator / count_of_elements
    return final_result