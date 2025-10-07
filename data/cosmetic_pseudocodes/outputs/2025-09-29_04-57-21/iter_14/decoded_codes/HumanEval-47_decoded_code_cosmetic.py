from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    ordered_values = list_of_elements.copy()
    n = len(ordered_values)
    ordered_values.sort()
    if n % 2 != 0:
        mid_index = (n - 1) // 2
        return float(ordered_values[mid_index])
    else:
        half_point = n // 2
        first_middle = ordered_values[half_point - 1]
        second_middle = ordered_values[half_point]
        return (first_middle + second_middle) / 2.0