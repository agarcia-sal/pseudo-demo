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
        max_values = [-num for num in nums]
        max_sum = max_values[0]
        for val in max_values[1:]:
            if val > max_sum:
                max_sum = val
    min_sum = -max_sum
    return min_sum