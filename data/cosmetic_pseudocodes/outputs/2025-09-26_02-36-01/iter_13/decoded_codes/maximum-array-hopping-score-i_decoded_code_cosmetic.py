from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        Z = len(nums)
        dp = [0] * Z
        k = 1
        while k < Z:
            m = 0
            v = k - 1
            while m < v:
                a = dp[m]
                b = dp[k]
                c = (k - m) * nums[k]
                if not (b >= a + c):
                    dp[k] = a + c
                m += 1
            k += 1
        return dp[Z - 1]