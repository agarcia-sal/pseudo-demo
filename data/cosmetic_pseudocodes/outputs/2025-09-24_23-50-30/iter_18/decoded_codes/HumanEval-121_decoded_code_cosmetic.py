from typing import List

def solution(arr: List[int]) -> int:
    total: int = 0
    counter: int = 0
    while counter < len(arr):
        current_val: int = arr[counter]
        # Check if counter is even and current_val is odd
        if (counter // 2) * 2 == counter and (current_val // 2) * 2 + 1 == current_val:
            total += current_val
        counter += 1
    return total