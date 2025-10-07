from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    ans: List[int] = []
    for i in range(len(arr) - k, len(arr)):
        ans.append(arr[i])
    return ans