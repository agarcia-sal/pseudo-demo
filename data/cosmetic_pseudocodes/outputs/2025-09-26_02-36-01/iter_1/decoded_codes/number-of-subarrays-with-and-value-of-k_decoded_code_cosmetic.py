from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total_subarrays = 0
        length = len(nums)
        for i in range(length):
            accum_and = nums[i]
            for j in range(i, length):
                accum_and &= nums[j]
                if accum_and == k:
                    total_subarrays += 1
                elif accum_and < k:
                    break
        return total_subarrays