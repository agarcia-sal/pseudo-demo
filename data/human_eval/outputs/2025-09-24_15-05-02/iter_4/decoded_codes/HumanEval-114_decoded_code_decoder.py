from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_sum = 0
    current_sum = 0

    for number in nums:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum

    if max_sum == 0:
        max_sum = max(-value for value in nums)

    min_sum = -max_sum
    return min_sum