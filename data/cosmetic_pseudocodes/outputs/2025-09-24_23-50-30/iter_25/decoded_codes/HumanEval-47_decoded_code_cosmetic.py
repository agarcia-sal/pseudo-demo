from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    count = len(sorted_list)
    mid = count // 2

    if count % 2 != 0:
        return float(sorted_list[mid])
    else:
        sum_pair = sorted_list[mid - 1] + sorted_list[mid]
        return sum_pair / 2.0