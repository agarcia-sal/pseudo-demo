from typing import List

def smallest_change(arr: List[int]) -> int:
    ans: int = 0
    n: int = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            ans += 1
    return ans