from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        size = len(nums)
        center = size // 2

        if nums[center] == k:
            return 0

        ops = 0
        if nums[center] < k:
            pos = center
            while pos < size and nums[pos] < k:
                ops += k - nums[pos]
                pos += 1
        else:
            idx = center
            while idx >= 0 and nums[idx] > k:
                ops += nums[idx] - k
                idx -= 1

        return ops