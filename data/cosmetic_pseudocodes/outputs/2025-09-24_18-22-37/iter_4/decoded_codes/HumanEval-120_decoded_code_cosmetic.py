from typing import List


def maximum(arr_ints: List[int], k_pos: int) -> List[int]:
    if k_pos == 0:
        return []
    arr_ints.sort()  # sort_non_decreasing
    start_index = len(arr_ints) - k_pos
    # slice the last k_pos elements after sorting
    return arr_ints[start_index:]