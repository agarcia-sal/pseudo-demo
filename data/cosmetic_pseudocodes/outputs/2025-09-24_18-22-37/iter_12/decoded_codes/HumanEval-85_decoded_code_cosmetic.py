from typing import Sequence

def add(nums: Sequence[int]) -> int:
    total: int = 0
    idx: int = 1
    while idx < len(nums):
        val: int = nums[idx]
        if val % 2 == 0:
            total += val
        idx += 2
    return total