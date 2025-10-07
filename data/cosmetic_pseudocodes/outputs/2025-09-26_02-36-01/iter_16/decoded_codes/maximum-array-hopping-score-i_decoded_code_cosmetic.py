from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        a = len(nums)
        b = [0] * a
        # The pseudocode sets b[1] = 0 explicitly, but it's already zero

        c = 2
        while c <= a:
            d = 1
            while d < c:
                e = b[d - 1] + ((c - d) * nums[c - 1])
                if b[c - 1] < e:
                    b[c - 1] = e
                d += 1
            c += 1

        return b[a - 1]