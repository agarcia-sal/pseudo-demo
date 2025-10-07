from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    sum_of_first_and_last: int = array[0] + array[-1]
    sort_in_descending_order: bool = (sum_of_first_and_last % 2 == 0)
    sorted_array: List[int] = sorted(array, reverse=sort_in_descending_order)
    return sorted_array