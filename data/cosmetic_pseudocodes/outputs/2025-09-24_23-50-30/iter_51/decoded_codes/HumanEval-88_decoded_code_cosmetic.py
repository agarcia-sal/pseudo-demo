from typing import List

def sort_array(arr: List[int]) -> List[int]:
    length = len(arr)
    if length == 0:
        return []
    alpha = arr[0]
    beta = arr[-1]
    gamma = (beta + alpha) % 2
    delta = gamma == 0
    return sorted(arr, reverse=delta)