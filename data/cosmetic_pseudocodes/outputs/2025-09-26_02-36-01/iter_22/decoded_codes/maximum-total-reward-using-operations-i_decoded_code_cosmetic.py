class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()

        from functools import lru_cache

        @lru_cache(None)
        def dfs(y):
            n = len(rewardValues)
            # Binary search to find smallest index idx where rewardValues[idx] > y
            low, high = 0, n
            while low < high:
                mid = low + (high - low) // 2
                if rewardValues[mid] <= y:
                    low = mid + 1
                else:
                    high = mid
            idx = low

            output = 0
            pos = idx
            while pos < n:
                value = rewardValues[pos]
                # Only proceed if y + value > y (avoids infinite or duplicate recursion)
                if y + value > y:
                    temp = dfs(y + value)
                    sumVal = temp + value
                    if sumVal > output:
                        output = sumVal
                pos += 1
            return output

        return dfs(0)