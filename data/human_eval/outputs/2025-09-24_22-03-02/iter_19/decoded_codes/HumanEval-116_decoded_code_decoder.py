from typing import List

def sort_array(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    sorted_arr_by_ones = sorted(sorted_arr, key=lambda x: bin(x)[2:].count('1'))
    return sorted_arr_by_ones