from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    sum_of_first_and_last = array[0] + array[-1]
    should_sort_in_descending = (sum_of_first_and_last % 2) == 0
    return sorted(array, reverse=should_sort_in_descending)