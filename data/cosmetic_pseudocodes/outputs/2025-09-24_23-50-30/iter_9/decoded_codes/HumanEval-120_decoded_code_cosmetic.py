from typing import List


def maximum(nums: List[int], count: int) -> List[int]:
    if count <= 0:
        return []
    nums_sorted = sorted(nums)
    return nums_sorted[-count:]