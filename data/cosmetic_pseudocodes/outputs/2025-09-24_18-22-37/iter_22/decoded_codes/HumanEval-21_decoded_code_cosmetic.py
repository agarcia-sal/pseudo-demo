from typing import List

def rescale_to_unit(values_array: List[float]) -> List[float]:
    if not values_array:
        return []
    smallest_value = values_array[0]
    largest_value = values_array[0]
    idx = 1
    while idx < len(values_array):
        v = values_array[idx]
        if v < smallest_value:
            smallest_value = v
        elif v > largest_value:
            largest_value = v
        idx += 1

    denominator = largest_value - smallest_value
    # Avoid division by zero if all values are the same
    if denominator == 0:
        return [0.0] * len(values_array)

    normalized_list: List[float] = []
    pos = 0
    while pos < len(values_array):
        numerator = values_array[pos] - smallest_value
        normalized_value = numerator / denominator
        normalized_list.append(normalized_value)
        pos += 1

    return normalized_list