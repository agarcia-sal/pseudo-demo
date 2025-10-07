from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum: int = 0
    current_sum: int = 0
    for num in nums:
        current_sum += -num
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum: int = -max_sum
    return min_sum