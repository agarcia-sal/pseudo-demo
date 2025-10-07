from typing import List, Any


def maximum(arr: List[Any], k: int) -> List[Any]:
    if k == 0:
        return []
    sorted_arr = sorted(arr)
    start_index = len(sorted_arr) - k
    return sorted_arr[start_index:]