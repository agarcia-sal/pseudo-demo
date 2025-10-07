from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    initial_last_sum = array[0] + array[-1]
    descending_flag = (initial_last_sum % 2 == 0)

    return sorted(array, reverse=descending_flag)