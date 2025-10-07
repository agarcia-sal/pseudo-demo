from math import floor
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        u = (n + 1) * n // 2  # total number of subarrays
        v = 0
        p = n

        def canMakeNonDecreasing(x: int, y: int) -> bool:
            d = 0
            e = nums[x]
            q = 1
            while q < y:
                r = nums[x + q]
                if r < e:
                    d += (e - r)
                e = e if e >= r else r
                if d > k:
                    return False
                q += 1
            return True

        def binSearch(a: int, b: int) -> int:
            left, right = a, b
            res = 0
            while left <= right:
                c = (left + right) // 2
                if canMakeNonDecreasing(a, c):
                    left = c + 1
                else:
                    right = c - 1
            return right

        m = 0
        while True:
            if m == p:
                break
            w = binSearch(m, p - m)
            v += (p - m - w)
            m += 1

        return u - v