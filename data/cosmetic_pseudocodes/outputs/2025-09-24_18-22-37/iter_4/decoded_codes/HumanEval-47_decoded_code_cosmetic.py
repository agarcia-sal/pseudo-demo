from typing import Sequence, Union

def median(input_array: Sequence[Union[int, float]]) -> float:
    sorted_array = sorted(input_array)
    n = len(sorted_array)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    if n % 2 != 0:
        middle_index = (n - 1) // 2
        return float(sorted_array[middle_index])
    else:
        first_middle = (n // 2) - 1
        second_middle = n // 2
        median_value = (sorted_array[first_middle] + sorted_array[second_middle]) / 2.0
        return median_value