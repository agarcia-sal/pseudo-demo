from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    arr_length = len(arr)
    start_index = arr_length - k
    for index in range(start_index, arr_length):
        ans.append(arr[index])
    return ans