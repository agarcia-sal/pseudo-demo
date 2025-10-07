from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        c = 0
        v = len(nums)
        w = target[0] - nums[0]
        if w < 0:
            w = -w
        c = w
        u = 1
        while u < v:
            a = target[u] - nums[u]
            b = target[u - 1] - nums[u - 1]
            if a * b > 0:
                m = a
                if m < 0:
                    m = -m
                n = b
                if n < 0:
                    n = -n
                z = m - n
                if z > 0:
                    c += z
            else:
                d = a
                if d < 0:
                    d = -d
                c += d
            u += 1
        return c