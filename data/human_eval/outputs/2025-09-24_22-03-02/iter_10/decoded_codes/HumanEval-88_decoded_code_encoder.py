from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_value = array[0] + array[-1]
    reverse_flag = (sum_value % 2 == 0)
    return sorted(array, reverse=reverse_flag)