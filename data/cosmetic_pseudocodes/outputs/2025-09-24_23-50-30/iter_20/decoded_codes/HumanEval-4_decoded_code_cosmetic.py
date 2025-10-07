from typing import Sequence

def mean_absolute_deviation(array_elements: Sequence[float]) -> float:
    count: int = len(array_elements)
    if count == 0:
        raise ValueError("array_elements must not be empty")
    accumulator: float = 0.0
    for index in range(count):
        accumulator += array_elements[index]
    average_value: float = accumulator / count

    deviations_sum: float = 0.0
    for element in array_elements:
        difference: float = element - average_value
        absolute_difference: float = difference if difference >= 0 else -difference
        deviations_sum += absolute_difference

    result: float = deviations_sum / count
    return result