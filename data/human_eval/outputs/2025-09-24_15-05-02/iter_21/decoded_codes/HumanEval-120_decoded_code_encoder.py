from typing import List

def maximum(array: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    array_sorted = sorted(array)
    answer = array_sorted[-k:]
    return answer