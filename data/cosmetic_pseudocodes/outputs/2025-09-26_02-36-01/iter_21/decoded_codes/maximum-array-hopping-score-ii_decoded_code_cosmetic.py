from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        q = len(nums)
        s = [0] * q
        u = q - 1
        while u >= 0:
            m = 0
            v = u + 1
            while v <= q - 1:
                val = (v - u) * nums[v] + s[v]
                if m < val:
                    m = val
                v += 1
            s[u] = m
            u -= 1
        return s[0]