import bisect

class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()

        def dfs(currentSum):
            insertionIndex = bisect.bisect_right(rewardValues, currentSum)
            highestReward = 0
            idx = insertionIndex
            while idx < len(rewardValues):
                candidateValue = rewardValues[idx]
                newSum = candidateValue + currentSum
                if newSum > currentSum:
                    recursiveResult = dfs(newSum)
                    combinedReward = candidateValue + recursiveResult
                    if combinedReward > highestReward:
                        highestReward = combinedReward
                idx += 1
            return highestReward

        return dfs(0)