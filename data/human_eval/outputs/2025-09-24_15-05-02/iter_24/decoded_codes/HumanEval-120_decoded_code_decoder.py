from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]