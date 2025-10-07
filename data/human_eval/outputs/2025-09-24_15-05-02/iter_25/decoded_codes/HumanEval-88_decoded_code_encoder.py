from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_of_first_and_last: int = array[0] + array[-1]
    if sum_of_first_and_last % 2 == 0:
        sorted_array: List[int] = sorted(array, reverse=True)
    else:
        sorted_array: List[int] = sorted(array)
    return sorted_array