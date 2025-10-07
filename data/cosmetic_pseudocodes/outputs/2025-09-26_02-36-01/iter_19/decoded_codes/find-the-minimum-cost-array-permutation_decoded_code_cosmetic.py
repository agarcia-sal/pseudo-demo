class Solution:
    def findPermutation(self, nums):
        from math import inf

        n = len(nums)
        full_mask = (1 << n) - 1
        memo = {}

        def recursiveSearch(stateFlag, lastIndex):
            if stateFlag == full_mask:
                return abs(nums[lastIndex] - nums[0])

            if (stateFlag, lastIndex) in memo:
                return memo[(stateFlag, lastIndex)]

            minimumResult = inf
            for idx in range(n):
                if ((stateFlag >> idx) & 1) == 0:
                    diff = abs(nums[lastIndex] - nums[idx])
                    totalCost = diff + recursiveSearch(stateFlag | (1 << idx), idx)
                    if totalCost < minimumResult:
                        minimumResult = totalCost
            memo[(stateFlag, lastIndex)] = minimumResult
            return minimumResult

        ans = []

        def gatherAnswers(selections, lastIndex):
            ans.append(nums[lastIndex])
            if selections == full_mask:
                return

            target = recursiveSearch(selections, lastIndex)
            for idx in range(n):
                if ((selections >> idx) & 1) == 0:
                    diff = abs(nums[lastIndex] - nums[idx])
                    candidateCost = diff + recursiveSearch(selections | (1 << idx), idx)
                    if candidateCost == target:
                        gatherAnswers(selections | (1 << idx), idx)
                        break

        gatherAnswers(1 << 0, 0)
        return ans