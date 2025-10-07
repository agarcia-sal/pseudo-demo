from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_of_ends = array[0] + array[len(array) - 1]
    sort_descending = (sum_of_ends % 2 == 0)
    return sorted(array, reverse=sort_descending)