from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_values: List[Union[int, float]] = sorted(list_of_elements)
    half_index: int = len(sorted_values) // 2
    if len(sorted_values) % 2 != 0:
        return float(sorted_values[half_index])
    else:
        return (sorted_values[half_index - 1] + sorted_values[half_index]) / 2.0