from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    length_of_arr = len(arr)
    start_index = length_of_arr - k
    for i in range(start_index, length_of_arr):
        ans.append(arr[i])
    return ans