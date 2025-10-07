from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    n = len(sorted_list)
    if n == 0:
        raise ValueError("median() arg is an empty list")
    if n % 2 == 1:
        return float(sorted_list[n // 2])
    else:
        middle_index = n // 2
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2.0