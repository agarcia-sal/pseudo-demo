from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    extreme_sum = array[0] + array[-1]
    descending_flag = (extreme_sum % 2) != 1  # True if even, False if odd
    return sorted(array, reverse=descending_flag)