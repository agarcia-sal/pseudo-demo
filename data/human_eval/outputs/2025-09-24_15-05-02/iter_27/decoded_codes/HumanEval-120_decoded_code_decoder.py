from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    if k < 0:
        raise ValueError("k must be non-negative")
    if k > len(arr):
        raise ValueError("k cannot be greater than the length of arr")
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]