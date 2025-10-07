from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    start_index = len(arr) - k
    end_index = len(arr) - 1
    for index in range(start_index, end_index + 1):
        ans.append(arr[index])
    return ans