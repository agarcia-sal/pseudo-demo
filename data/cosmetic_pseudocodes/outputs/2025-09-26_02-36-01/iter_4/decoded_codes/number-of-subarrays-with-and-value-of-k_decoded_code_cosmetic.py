from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalSubarrays = 0
        lengthNums = len(nums)
        i = 0
        while i <= lengthNums - 1:
            andAccumulator = nums[i]
            j = i
            while j <= lengthNums - 1:
                andAccumulator &= nums[j]
                if andAccumulator == k:
                    totalSubarrays += 1
                if andAccumulator < k:
                    break
                j += 1
            i += 1
        return totalSubarrays