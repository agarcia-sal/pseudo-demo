from typing import List

def maximum(arr: List[int], count: int) -> List[int]:
    if count != 0:
        arr_sorted = sorted(arr)
        start_idx = len(arr_sorted) - count
        result = arr_sorted[start_idx:]
    else:
        result = []
    return result