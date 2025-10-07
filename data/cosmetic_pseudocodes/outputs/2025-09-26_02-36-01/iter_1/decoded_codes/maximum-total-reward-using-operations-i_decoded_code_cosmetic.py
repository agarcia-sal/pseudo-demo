from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        from functools import lru_cache

        @lru_cache(None)
        def dfs(currentSum: int) -> int:
            idx = bisect_right(rewardValues, currentSum)
            maxReward = 0
            for index in range(idx, len(rewardValues)):
                nextVal = rewardValues[index]
                if currentSum + nextVal > currentSum:
                    candidate = nextVal + dfs(currentSum + nextVal)
                    if candidate > maxReward:
                        maxReward = candidate
            return maxReward

        return dfs(0)