from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    reverse_order = (sum_first_last % 2 == 0)
    return sorted(array, reverse=reverse_order)