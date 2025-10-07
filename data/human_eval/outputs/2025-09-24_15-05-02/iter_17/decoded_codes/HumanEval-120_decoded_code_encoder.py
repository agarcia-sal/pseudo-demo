from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr_sorted = sorted(arr)
    ans = arr_sorted[len(arr) - k:]
    return ans