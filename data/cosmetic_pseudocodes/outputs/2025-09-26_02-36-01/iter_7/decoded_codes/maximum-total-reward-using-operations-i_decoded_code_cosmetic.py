class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()  # Sort the list efficiently with built-in sort

        from functools import lru_cache

        n = len(rewardValues)

        @lru_cache(None)
        def dfs(y):
            # Binary search for insert position where rewardValues[pos] > y
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if rewardValues[mid] <= y:
                    left = mid + 1
                else:
                    right = mid - 1
            insertPos = left

            maxReward = 0
            idx = insertPos
            while idx < n:
                currentVal = rewardValues[idx]
                combinedSum = y + currentVal
                if combinedSum > y:
                    candidateReward = currentVal + dfs(combinedSum)
                    if candidateReward > maxReward:
                        maxReward = candidateReward
                idx += 1
            return maxReward

        return dfs(0)