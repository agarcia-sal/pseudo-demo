from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tally = 0

        for start in range(n):
            acc_and = nums[start]
            if acc_and == k:
                tally += 1
            if acc_and < k:
                continue
            for end in range(start + 1, n):
                acc_and &= nums[end]
                if acc_and == k:
                    tally += 1
                if acc_and < k:
                    break

        return tally