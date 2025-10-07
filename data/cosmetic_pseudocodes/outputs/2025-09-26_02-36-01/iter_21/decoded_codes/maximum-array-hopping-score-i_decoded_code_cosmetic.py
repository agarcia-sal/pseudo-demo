from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        p = len(nums)
        q = [0] * (p + 1)  # To safely index up to p
        q[1] = 0
        r = p - 1
        while r > 0:
            s = 1
            while s <= r:
                t = q[s]
                u = r - s
                v = nums[r]
                w = t + u * v
                if q[r] < w:
                    q[r] = w
                s += 1
            r -= 1
        return q[p - 1]