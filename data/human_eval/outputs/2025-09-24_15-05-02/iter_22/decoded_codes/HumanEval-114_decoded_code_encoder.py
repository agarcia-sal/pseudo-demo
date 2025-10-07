from typing import List

def minSubArraySum(nums: List[int]) -> int:
    max_subarray_sum: int = 0
    current_sum: int = 0
    for number in nums:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_subarray_sum:
            max_subarray_sum = current_sum
    if max_subarray_sum == 0:
        max_subarray_sum = max(-num for num in nums)
    min_subarray_sum: int = -max_subarray_sum
    return min_subarray_sum