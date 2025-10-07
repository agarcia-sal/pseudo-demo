from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        m = len(nums)

        def canMakeNonDecreasing(x: int, y: int) -> bool:
            p = 0
            q = nums[x]
            r = 1
            while r < y:
                s = nums[x + r]
                if s < q:
                    p += (q - s)
                if q < s:
                    q = s
                if p > k:
                    return False
                r += 1
            return True

        a = m * (m + 1) // 2
        b = 0

        c = 0
        while c < m:
            d = 1
            e = m - c
            while d <= e:
                f = (d + e) // 2
                if canMakeNonDecreasing(c, f):
                    d = f + 1
                else:
                    e = f - 1
            b += m - c - e
            c += 1

        return a - b