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
        max_temp = -nums[0]
        for index in range(1, len(nums)):
            i = nums[index]
            neg_i = -i
            if neg_i > max_temp:
                max_temp = neg_i
        max_sum = max_temp
    min_sum = -max_sum
    return min_sum