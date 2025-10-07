from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for start in range(n):
            current_and = nums[start]
            for end in range(start, n):
                current_and &= nums[end]
                if current_and == k:
                    count += 1
                if current_and < k:
                    break
        return count