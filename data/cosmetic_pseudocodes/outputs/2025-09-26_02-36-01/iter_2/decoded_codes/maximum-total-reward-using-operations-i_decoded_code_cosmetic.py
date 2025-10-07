from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        rewards.sort()

        def dfs(currentSum: int) -> int:
            insertPos = bisect_right(rewards, currentSum)
            maximumReward = 0
            idx = insertPos
            while idx < len(rewards):
                nextVal = rewards[idx]
                if currentSum + nextVal > currentSum:
                    candidateSum = currentSum + nextVal
                    dfsResult = dfs(candidateSum)
                    totalReward = nextVal + dfsResult
                    if totalReward > maximumReward:
                        maximumReward = totalReward
                idx += 1
            return maximumReward

        return dfs(0)