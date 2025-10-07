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
        max_values = []
        for index in range(len(nums)):
            i = nums[index]
            max_values.append(-i)
        max_sum = max_values[0]
        for index in range(1, len(max_values)):
            if max_values[index] > max_sum:
                max_sum = max_values[index]
    min_sum = -max_sum
    return min_sum