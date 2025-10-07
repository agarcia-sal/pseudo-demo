from typing import List

def smallest_change(arr: List[int]) -> int:
    ans = 0
    length = len(arr)
    for i in range(length // 2):
        if arr[i] != arr[length - i - 1]:
            ans += 1
    return ans