from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    first_last_sum: int = array[0] + array[-1]
    descending_order_flag: bool = (first_last_sum % 2) == 0
    return sorted(array, reverse=descending_order_flag)