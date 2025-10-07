from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    edge_sum = array[0] + array[-1]
    descending_flag = (edge_sum % 2 == 0)
    return sorted(array, reverse=descending_flag)