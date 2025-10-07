from bisect import insort
from typing import List, Union

def median(array_of_vals: List[Union[int, float]]) -> float:
    ordered_vals: List[Union[int, float]] = []
    for val in array_of_vals:
        insort(ordered_vals, val)  # Insert while keeping the list sorted

    size = len(ordered_vals)
    if size == 0:
        raise ValueError("median() arg is an empty sequence")

    if size % 2 != 0:
        middle_pos = (size - 1) // 2
        return float(ordered_vals[middle_pos])

    first_mid = ordered_vals[size // 2 - 1]
    second_mid = ordered_vals[size // 2]
    return (first_mid + second_mid) / 2.0