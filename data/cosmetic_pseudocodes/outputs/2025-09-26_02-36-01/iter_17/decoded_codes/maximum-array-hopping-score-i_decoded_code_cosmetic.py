from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        a = len(nums)
        b = [0] * a
        b[0] = 0
        x = 2
        while x <= a:
            y = 1
            while y < x:
                u = b[y - 1] + (x - y) * nums[x - 1]
                if b[x - 1] < u:
                    b[x - 1] = u
                y += 1
            x += 1
        return b[a - 1]