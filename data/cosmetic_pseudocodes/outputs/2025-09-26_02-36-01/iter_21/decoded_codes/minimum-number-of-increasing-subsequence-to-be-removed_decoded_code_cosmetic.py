from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = len(nums)
        if a == 0:
            return 0
        c = [1] * a
        d = a - 1
        while d > 0:
            e = 0
            while e < d:
                if not (nums[d] > nums[e]):
                    g = c[e] + 1
                    if g > c[d]:
                        c[d] = g
                e += 1
            d -= 1
        h = -1
        i = 0
        while i < a:
            if c[i] > h:
                h = c[i]
            i += 1
        return h