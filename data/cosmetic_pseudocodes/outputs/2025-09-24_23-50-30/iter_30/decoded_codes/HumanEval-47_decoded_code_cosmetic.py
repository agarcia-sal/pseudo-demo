from typing import List, Union

def median(list_input: List[Union[int, float]]) -> float:
    sorted_collection = sorted(list_input)
    size = len(sorted_collection)
    if size == 0:
        raise ValueError("median() arg is an empty list")
    if size % 2 == 0:
        half_idx = size // 2
        return (sorted_collection[half_idx - 1] + sorted_collection[half_idx]) / 2.0
    else:
        return float(sorted_collection[(size - 1) // 2])