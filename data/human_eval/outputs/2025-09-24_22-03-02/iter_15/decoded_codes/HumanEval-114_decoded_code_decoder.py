from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        temporary_list = []
        for i in nums:
            temporary_list.append(-i)
        max_sum = max(temporary_list)
    min_sum = -max_sum
    return min_sum