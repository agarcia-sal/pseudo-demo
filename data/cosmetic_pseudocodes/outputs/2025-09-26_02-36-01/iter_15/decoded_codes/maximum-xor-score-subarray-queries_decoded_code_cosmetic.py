from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        u = len(nums)
        h = [[0] * u for _ in range(u)]
        v = [[0] * u for _ in range(u)]

        c = u - 1
        while c >= 0:
            h[c][c] = nums[c]
            v[c][c] = nums[c]
            d = c + 1
            while d < u:
                m = h[c][d - 1] ^ h[c + 1][d]
                h[c][d] = m
                v[c][d] = max(v[c][d], h[c][d])
                v[c][d] = max(v[c][d], v[c][d - 1])
                v[c][d] = max(v[c][d], v[c + 1][d])
                d += 1
            c -= 1

        r = []
        for s, t in queries:
            r.append(v[s][t])
        return r