from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    boundary_sum = array[-1] + array[0]
    descending_flag = (boundary_sum % 2) == 0
    return sorted(array, reverse=descending_flag)