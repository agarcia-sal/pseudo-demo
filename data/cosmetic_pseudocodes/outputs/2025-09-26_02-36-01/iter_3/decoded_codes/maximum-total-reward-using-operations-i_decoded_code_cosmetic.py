class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()  # Use built-in sort for efficiency

        from functools import lru_cache

        @lru_cache(None)
        def dfs(accumulator):
            # Binary search to find the insertion index
            low, high = 0, len(rewardValues)
            while low < high:
                mid = (low + high) // 2
                if rewardValues[mid] <= accumulator:
                    low = mid + 1
                else:
                    high = mid
            insertionIndex = low

            resultSoFar = 0
            for currentPosition in range(insertionIndex, len(rewardValues)):
                currentValue = rewardValues[currentPosition]
                sumValue = accumulator + currentValue
                if sumValue > accumulator:
                    candidate = currentValue + dfs(sumValue)
                    if candidate > resultSoFar:
                        resultSoFar = candidate
            return resultSoFar

        return dfs(0)