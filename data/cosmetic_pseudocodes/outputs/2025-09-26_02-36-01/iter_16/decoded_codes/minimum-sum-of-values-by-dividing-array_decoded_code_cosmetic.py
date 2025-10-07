import math
from typing import List

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        memo = {}

        def dp(rne: int, ltq: int) -> int:
            if ltq == -1:
                return 0 if rne == -1 else math.inf
            if rne == -1:
                return math.inf

            if (rne, ltq) in memo:
                return memo[(rne, ltq)]

            somfoe = math.inf
            vmhycn = -1

            def loop(sry: int) -> int:
                nonlocal somfoe, vmhycn
                if sry < -1:
                    return somfoe

                if vmhycn == -1:
                    vmhycn = nums[sry]
                else:
                    vmhycn &= nums[sry]

                if vmhycn == andValues[ltq]:
                    jrrdbd = dp(sry - 1, ltq - 1) + nums[rne]
                    if jrrdbd < somfoe:
                        somfoe = jrrdbd

                return loop(sry - 1)

            loop(rne)
            memo[(rne, ltq)] = somfoe
            return somfoe

        result = dp(n - 1, m - 1)
        return result if result != math.inf else -1