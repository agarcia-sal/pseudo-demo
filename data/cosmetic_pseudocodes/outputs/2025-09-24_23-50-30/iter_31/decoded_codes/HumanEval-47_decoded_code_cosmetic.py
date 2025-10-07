from typing import Sequence, Union

def median(array_input: Sequence[float]) -> float:
    array_sorted = sorted(array_input)
    length_val = len(array_sorted)
    is_odd = (length_val % 2) != 0
    if is_odd:
        return array_sorted[(length_val - 1) // 2]
    else:
        return (array_sorted[(length_val // 2) - 1] + array_sorted[length_val // 2]) / 2.0