class Solution:
    def numberOfPermutations(self, n, requirements):
        MODULO = 1_000_000_007
        requirementMap = {endIndex: count for endIndex, count in requirements}

        def dfs(currentIndex, currentInversions, mask):
            if currentIndex == n:
                targetInv = requirementMap.get(n, 0)
                return 1 if currentInversions == targetInv else 0

            if currentIndex > 0:
                expectedInv = requirementMap.get(currentIndex, currentInversions)
                if currentInversions != expectedInv:
                    return 0

            totalWays = 0
            for candidate in range(n):
                if (mask & (1 << candidate)) == 0:
                    updatedInv = currentInversions
                    for later in range(candidate + 1, n):
                        if (mask & (1 << later)) != 0:
                            updatedInv += 1
                    totalWays = (totalWays + dfs(currentIndex + 1, updatedInv, mask | (1 << candidate))) % MODULO
            return totalWays

        return dfs(0, 0, 0)