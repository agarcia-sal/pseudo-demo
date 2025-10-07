from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_boundary_values = array[0] + array[len(array) - 1]
    if sum_boundary_values % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)
    return sorted_array