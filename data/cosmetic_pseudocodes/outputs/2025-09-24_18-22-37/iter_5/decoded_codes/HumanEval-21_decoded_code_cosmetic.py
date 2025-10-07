from typing import List


def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    if not array_of_values:
        return []
    idx: int = 0
    min_val: float = array_of_values[0]
    max_val: float = array_of_values[0]

    while idx < len(array_of_values):
        val = array_of_values[idx]
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
        idx += 1

    scaled_array: List[float] = []
    range_val: float = max_val - min_val
    pos: int = 0

    # Avoid division by zero if all values are the same
    if range_val == 0:
        return [0.0 for _ in array_of_values]

    while pos < len(array_of_values):
        numerator: float = array_of_values[pos] - min_val
        ratio: float = numerator / range_val
        scaled_array.append(ratio)
        pos += 1

    return scaled_array