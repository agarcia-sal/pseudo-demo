from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum = 0
    current_sum = 0
    for num in nums:
        current_sum += -num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    if max_sum == 0:
        max_sum = max(-num for num in nums)
    min_sum = -max_sum
    return min_sum