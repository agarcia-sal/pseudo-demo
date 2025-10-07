from typing import Sequence, Union

def median(array_input: Sequence[Union[int, float]]) -> float:
    sorted_array = sorted(array_input)
    size = len(sorted_array)
    midpoint = size // 2

    if size % 2 != 0:
        return float(sorted_array[midpoint])

    lower_mid = sorted_array[midpoint - 1]
    upper_mid = sorted_array[midpoint]
    median_result = (lower_mid + upper_mid) / 2.0
    return median_result