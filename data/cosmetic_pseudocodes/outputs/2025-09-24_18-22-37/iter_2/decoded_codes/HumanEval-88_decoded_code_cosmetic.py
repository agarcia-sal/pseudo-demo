from typing import List

def sort_array(arr: List[int]) -> List[int]:
    if not arr:
        return []

    boundary_sum = arr[0] + arr[-1]
    descending_flag = (boundary_sum % 2) == 0

    result = sorted(arr)
    if descending_flag:
        result.reverse()

    return result