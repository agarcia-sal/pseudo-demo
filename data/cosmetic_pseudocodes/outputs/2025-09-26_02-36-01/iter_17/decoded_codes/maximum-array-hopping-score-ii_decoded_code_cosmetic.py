from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        x = len(nums)
        y = [0] * x
        a = x - 2
        while a >= 0:
            b = 0
            c = a + 1
            while c < x:
                d = c - a
                e = nums[c] * d
                f = e + y[c]
                if b < f:
                    b = f
                c += 1
            y[a] = b
            a -= 1
        return y[0]