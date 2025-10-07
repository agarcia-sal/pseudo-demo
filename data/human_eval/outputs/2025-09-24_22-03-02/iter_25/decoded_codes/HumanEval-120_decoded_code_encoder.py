from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    length_arr = len(arr)
    start_index = length_arr - k
    end_index = length_arr - 1
    ans = []
    for i in range(start_index, end_index + 1):
        ans.append(arr[i])
    return ans