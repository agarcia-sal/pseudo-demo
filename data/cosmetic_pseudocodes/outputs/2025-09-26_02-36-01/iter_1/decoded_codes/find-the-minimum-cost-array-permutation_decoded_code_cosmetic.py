class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        ans = []

        from functools import lru_cache

        @lru_cache(None)
        def dfs(currentMask, previousIndex):
            if currentMask == (1 << n) - 1:
                return abs(nums[previousIndex] - nums[0])

            minimumCost = float('inf')
            for index in range(n):
                if ((currentMask >> index) & 1) == 0:
                    nextMask = currentMask | (1 << index)
                    cost = abs(nums[previousIndex] - nums[index]) + dfs(nextMask, index)
                    if cost < minimumCost:
                        minimumCost = cost
            return minimumCost

        def buildPath(mask, prev):
            ans.append(prev)
            if mask == (1 << n) - 1:
                return

            targetCost = dfs(mask, prev)
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    candidateMask = mask | (1 << i)
                    candidateCost = abs(nums[prev] - nums[i]) + dfs(candidateMask, i)
                    if candidateCost == targetCost:
                        buildPath(candidateMask, i)
                        break

        buildPath(1 << 0, 0)
        return ans