from typing import List

def smallest_change(arr: List[int]) -> int:
    count: int = 0
    limit: int = len(arr) // 2
    for i in range(limit):
        left_val: int = arr[i]
        right_val: int = arr[len(arr) - (i + 1)]
        if left_val != right_val:
            count += 1
    return count