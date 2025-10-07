from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        totalCount = 0
        i = 0
        while i < length:
            andValue = nums[i]
            j = i
            while j < length:
                andValue &= nums[j]
                if andValue == k:
                    totalCount += 1
                if andValue < k:
                    break
                j += 1
            i += 1
        return totalCount