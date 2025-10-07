from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    left_index: int = 0
    right_index: int = len(array) - 1
    sum_ends: int = array[left_index] + array[right_index]
    is_even: bool = (sum_ends % 2) == 0
    return sorted(array, reverse=is_even)