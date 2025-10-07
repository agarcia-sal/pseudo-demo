from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = list(list_of_elements)  # copy list to avoid mutating input
    sorted_list.sort()
    n = len(sorted_list)
    if n % 2 != 0:
        middle_position = (n - 1) // 2
        return float(sorted_list[middle_position])
    else:
        lower_middle = (n // 2) - 1
        upper_middle = n // 2
        sum_of_middles = sorted_list[lower_middle] + sorted_list[upper_middle]
        return sum_of_middles * 0.5