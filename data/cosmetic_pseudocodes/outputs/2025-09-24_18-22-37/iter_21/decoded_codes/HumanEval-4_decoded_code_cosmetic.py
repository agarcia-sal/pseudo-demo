from typing import Sequence

def mean_absolute_deviation(sequence_elements: Sequence[float]) -> float:
    total_sum: float = 0
    count_elements: int = 0
    for element in sequence_elements:
        total_sum += element
        count_elements += 1

    if count_elements == 0:
        raise ZeroDivisionError("mean_absolute_deviation() arg is an empty sequence")

    average: float = total_sum / count_elements

    deviation_sum: float = 0
    index: int = 0
    while index < count_elements:
        difference: float = sequence_elements[index] - average
        absolute_difference: float = difference
        if absolute_difference < 0:
            absolute_difference = -absolute_difference
        deviation_sum += absolute_difference
        index += 1

    mad_result: float = deviation_sum / count_elements
    return mad_result