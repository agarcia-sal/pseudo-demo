from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    sort_descending = (sum_first_last % 2 == 0)
    return sorted(array, reverse=sort_descending)