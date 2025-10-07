from typing import List

def incr_list(arr: List[int]) -> List[int]:
    idx: int = 0
    result: List[int] = []
    while idx < len(arr):
        result.append(arr[idx] + 1)
        idx += 1
    return result