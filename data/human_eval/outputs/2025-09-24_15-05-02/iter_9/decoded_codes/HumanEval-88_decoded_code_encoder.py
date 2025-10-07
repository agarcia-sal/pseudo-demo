from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_endpoints = array[0] + array[-1]
    descending_order = sum_endpoints % 2 == 0
    return sorted(array, reverse=descending_order)