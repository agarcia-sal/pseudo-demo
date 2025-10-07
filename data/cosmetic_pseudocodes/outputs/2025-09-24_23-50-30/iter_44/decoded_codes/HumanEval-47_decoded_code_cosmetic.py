from typing import Sequence, Union

def median(array_data: Sequence[Union[int, float]]) -> float:
    sorted_array = sorted(array_data)
    size = len(sorted_array)
    if size % 2 != 0:
        return float(sorted_array[size // 2])
    idx = size // 2
    return (sorted_array[idx - 1] + sorted_array[idx]) * 0.5