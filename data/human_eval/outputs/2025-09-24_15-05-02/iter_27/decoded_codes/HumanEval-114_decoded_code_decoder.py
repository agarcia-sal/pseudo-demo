from typing import List

def minSubArraySum(nums: List[int]) -> int:
    if not nums:
        raise ValueError("Input list 'nums' must not be empty.")
    max_sum: int = 0
    s: int = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum: int = -max_sum
    return min_sum