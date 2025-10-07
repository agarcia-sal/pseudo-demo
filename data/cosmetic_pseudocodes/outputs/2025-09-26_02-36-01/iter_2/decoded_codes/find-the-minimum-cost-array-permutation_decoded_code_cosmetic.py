from math import inf

class Solution:
    def findPermutation(self, inputList):
        n = len(inputList)
        memo = {}

        def dfs(usedBits, lastIndex):
            if usedBits == (1 << n) - 1:
                diff = lastIndex - 0
                return abs(diff)
            if (usedBits, lastIndex) in memo:
                return memo[(usedBits, lastIndex)]

            minimumResult = inf
            for idx in range(n):
                if ((usedBits >> idx) & 1) == 0:
                    costPart = abs(lastIndex - idx)
                    nextCall = dfs(usedBits | (1 << idx), idx)
                    totalCost = costPart + nextCall
                    if totalCost < minimumResult:
                        minimumResult = totalCost
            memo[(usedBits, lastIndex)] = minimumResult
            return minimumResult

        ans = []

        def g(maskFlag, previousIndex):
            ans.append(previousIndex)
            if maskFlag == (1 << n) - 1:
                return
            targetValue = dfs(maskFlag, previousIndex)
            for counter in range(n):
                if ((maskFlag >> counter) & 1) == 0:
                    diffVal = abs(previousIndex - counter)
                    retVal = dfs(maskFlag | (1 << counter), counter)
                    candidateCost = diffVal + retVal
                    if candidateCost == targetValue:
                        g(maskFlag | (1 << counter), counter)
                        break

        g(1 << 0, 0)
        return ans