from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_diff = float('inf')
        for start in range(n):
            current_or = 0
            for end in range(start, n):
                current_or |= nums[end]
                diff = abs(k - current_or)
                if diff < min_diff:
                    min_diff = diff
                if diff == 0:
                    return 0
        return min_diff