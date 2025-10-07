from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []

    boundary_sum: int = array[0] + array[-1]
    is_descending_order: bool = (boundary_sum % 2) == 0

    return sorted(array, reverse=is_descending_order)