from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        from functools import lru_cache

        @lru_cache(None)
        def dfs(x: int) -> int:
            i = bisect_right(rewardValues, x)
            ans = 0
            for v in rewardValues[i:]:
                # Since v > x (because i is bisect_right position),
                # sum of x and v is always > x, so this check is guaranteed.
                candidate = v + dfs(x + v)
                if candidate > ans:
                    ans = candidate
            return ans

        return dfs(0)