from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        u = len(nums)
        v = [0] * u
        if u < 2:
            return 0
        v[1] = 0
        x = 2
        while x <= u - 1:
            y = 1
            while y < x:
                a = v[x]
                b = v[y] + (x - y) * nums[x]
                if a < b:
                    v[x] = b
                y += 1
            x += 1
        return v[u - 1]