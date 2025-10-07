from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr_sorted = sorted(arr)
    return arr_sorted[len(arr) - k :]