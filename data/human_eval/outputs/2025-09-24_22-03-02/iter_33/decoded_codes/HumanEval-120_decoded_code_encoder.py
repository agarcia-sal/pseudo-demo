from typing import List, Any

def maximum(arr: List[Any], k: int) -> List[Any]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    n = len(arr)
    start_index = n - k
    i = start_index
    while i < n:
        ans.append(arr[i])
        i += 1
    return ans