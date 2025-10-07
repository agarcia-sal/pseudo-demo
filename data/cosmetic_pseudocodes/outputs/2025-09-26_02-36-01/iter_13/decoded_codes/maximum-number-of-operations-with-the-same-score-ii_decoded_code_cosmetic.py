from functools import lru_cache
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        p0 = nums[0] + nums[1]
        p1 = nums[n - 2] + nums[n - 1]
        p2 = nums[0] + nums[n - 1]

        def helper(a: int, b: int, c: int) -> int:
            if a >= b:
                return 0

            @lru_cache(None)
            def recur(x: int, y: int, z: int) -> int:
                if x >= y:
                    return 0
                best = 0
                if nums[x] + nums[x + 1] == z:
                    best = max(best, 1 + recur(x + 2, y, z))
                if nums[y] + nums[y - 1] == z:
                    best = max(best, 1 + recur(x, y - 2, z))
                if nums[x] + nums[y] == z:
                    best = max(best, 1 + recur(x + 1, y - 1, z))
                return best

            return 1 + recur(a, b, c)

        res1 = helper(2, n - 1, p0)
        res2 = helper(0, n - 3, p1)
        res3 = helper(1, n - 2, p2)

        if res1 > res2:
            return res1 if res1 > res3 else res3
        else:
            return res2 if res2 > res3 else res3