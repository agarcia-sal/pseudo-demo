from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    for index in range(len(arr) - k, len(arr)):
        ans.append(arr[index])
    return ans