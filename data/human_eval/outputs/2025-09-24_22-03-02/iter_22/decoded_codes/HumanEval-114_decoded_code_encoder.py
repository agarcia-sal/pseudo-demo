from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_negative = -nums[0]
        for num in nums:
            if -num > max_negative:
                max_negative = -num
        max_sum = max_negative
    min_sum = -max_sum
    return min_sum