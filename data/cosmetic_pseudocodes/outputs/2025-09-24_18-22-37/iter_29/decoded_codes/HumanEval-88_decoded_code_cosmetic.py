from typing import List

def sort_array(arr: List[int]) -> List[int]:
    idx_1: int = len(arr) - 1

    if len(arr) != 0:
        sum_edges: int = arr[0] + arr[idx_1]
        desc_flag: bool = (sum_edges % 2) != 1  # True if sum_edges is even
        return sorted(arr, reverse=desc_flag)

    return []