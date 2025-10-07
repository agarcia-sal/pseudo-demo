from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        i = 0
        while i < n:
            curr = nums[i]
            j = i
            while j < n:
                curr &= nums[j]
                if curr == k:
                    count += 1
                if curr < k:
                    break
                j += 1
            i += 1
        return count