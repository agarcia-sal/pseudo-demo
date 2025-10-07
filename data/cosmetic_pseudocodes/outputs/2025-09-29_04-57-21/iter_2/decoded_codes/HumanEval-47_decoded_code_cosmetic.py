from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> Union[int, float]:
    ordered_values = list(list_of_elements)
    ordered_values.sort()
    total_count = len(ordered_values)
    midpoint = total_count // 2
    if (total_count - 1) % 2 != 0:
        return ordered_values[midpoint]
    else:
        left_mid = ordered_values[midpoint - 1]
        right_mid = ordered_values[midpoint]
        return (left_mid + right_mid) * 0.5