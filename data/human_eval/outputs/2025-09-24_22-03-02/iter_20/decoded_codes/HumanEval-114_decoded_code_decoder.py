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
        max_element = -nums[0]
        for num in nums[1:]:
            if -num > max_element:
                max_element = -num
        max_sum = max_element
    min_sum = -max_sum
    return min_sum