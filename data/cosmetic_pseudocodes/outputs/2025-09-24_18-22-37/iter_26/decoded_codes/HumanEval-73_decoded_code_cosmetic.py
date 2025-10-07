from typing import List

def smallest_change(arr: List[int]) -> int:
    count_diff = 0
    half_len = (len(arr) // 2) - 1  # integer division for midpoint adjustment
    pos = 0
    while pos <= half_len:
        left_val = arr[pos]
        right_index = len(arr) - pos - 1
        right_val = arr[right_index]
        if left_val != right_val:
            count_diff += 1
        pos += 1
    return count_diff