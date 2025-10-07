from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    total = array[0] + array[-1]
    descending_flag = (total % 2 == 0)
    return sorted(array, reverse=descending_flag)