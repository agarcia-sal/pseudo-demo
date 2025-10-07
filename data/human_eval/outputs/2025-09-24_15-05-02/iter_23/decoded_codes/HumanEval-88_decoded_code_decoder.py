from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_of_ends: int = array[0] + array[-1]
    sort_in_descending_order: bool = (sum_of_ends % 2 == 0)
    return sorted(array, reverse=sort_in_descending_order)