from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    n = len(sorted_list)
    if n % 2 == 1:
        return float(sorted_list[n // 2])
    else:
        middle_left = sorted_list[(n // 2) - 1]
        middle_right = sorted_list[n // 2]
        return (middle_left + middle_right) / 2.0