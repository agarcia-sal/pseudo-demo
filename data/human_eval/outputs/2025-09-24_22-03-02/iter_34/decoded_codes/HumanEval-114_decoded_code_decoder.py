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
        max_temp = -nums[0]
        for i in range(1, len(nums)):
            current_value = -nums[i]
            if current_value > max_temp:
                max_temp = current_value
        max_sum = max_temp
    min_sum = -max_sum
    return min_sum