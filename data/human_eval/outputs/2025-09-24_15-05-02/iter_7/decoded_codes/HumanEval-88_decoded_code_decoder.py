from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []

    sum_of_endpoints = array[0] + array[-1]
    sort_in_descending = (sum_of_endpoints % 2 == 0)

    sorted_array = sorted(array, reverse=sort_in_descending)
    return sorted_array