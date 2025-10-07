from typing import List

def maximum(array: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    array.sort()
    ans = array[-k:]
    return ans