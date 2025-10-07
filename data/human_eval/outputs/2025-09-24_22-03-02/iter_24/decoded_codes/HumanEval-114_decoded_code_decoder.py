from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum = 0
    s = 0
    for index in range(len(nums)):
        num = nums[index]
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_neg = -nums[0]
        for index in range(1, len(nums)):
            candidate = -nums[index]
            if candidate > max_neg:
                max_neg = candidate
        max_sum = max_neg
    min_sum = -max_sum
    return min_sum