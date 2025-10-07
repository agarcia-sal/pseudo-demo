from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        start = 0
        while start < n:
            current_and = nums[start]
            end = start
            while end < n:
                current_and &= nums[end]
                if current_and == k:
                    result += 1
                if current_and < k:
                    break
                end += 1
            start += 1
        return result