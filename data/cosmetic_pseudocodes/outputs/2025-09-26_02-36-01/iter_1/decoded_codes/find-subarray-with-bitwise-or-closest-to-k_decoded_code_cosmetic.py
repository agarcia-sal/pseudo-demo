from math import inf
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        array_length = len(nums)
        closest_difference = inf

        for left_index in range(array_length):
            accumulated_or = 0
            for right_index in range(left_index, array_length):
                accumulated_or |= nums[right_index]
                current_diff = abs(k - accumulated_or)
                if current_diff < closest_difference:
                    closest_difference = current_diff
                if current_diff == 0:
                    return 0

        return closest_difference