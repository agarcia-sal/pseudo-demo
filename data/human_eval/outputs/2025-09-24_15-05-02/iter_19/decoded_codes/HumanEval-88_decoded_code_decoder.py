from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_of_ends: int = array[0] + array[-1]
    should_sort_descending: bool = (sum_of_ends % 2 == 0)
    return sorted(array, reverse=should_sort_descending)