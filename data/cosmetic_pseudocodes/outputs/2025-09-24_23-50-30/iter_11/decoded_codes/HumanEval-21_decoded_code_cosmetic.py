from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    min_val: float = array_of_values[0]
    max_val: float = array_of_values[0]
    for idx in range(1, len(array_of_values)):
        if array_of_values[idx] < min_val:
            min_val = array_of_values[idx]
        if array_of_values[idx] > max_val:
            max_val = array_of_values[idx]

    diff = max_val - min_val
    if diff == 0:
        return [0.0] * len(array_of_values)  # Avoid division by zero, all values equal

    return [(val - min_val) / diff for val in array_of_values]