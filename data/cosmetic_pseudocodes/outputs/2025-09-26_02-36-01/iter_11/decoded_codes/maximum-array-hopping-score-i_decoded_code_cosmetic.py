from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        s = len(nums) - 1
        dp = [0] * (s + 1)
        dp[1] = 0

        def helper(p: int) -> int:
            if p == 1:
                return 0
            y = helper(p - 1)
            z = 0
            for x in range(1, p):
                val = dp[x] + (p - x) * nums[p]
                if dp[p] < val:
                    z = val
                    dp[p] = z
            return dp[p]

        for k in range(1, s + 1):
            helper(k)
        return dp[s]