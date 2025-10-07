class Solution:
    def numberOfPermutations(self, n, requirements):
        M = 10**9 + 7
        mapping = {}
        for index, quantity in requirements:
            mapping[index] = quantity

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(depth, inversionCount, usedMask):
            if depth == n:
                return 1 if inversionCount == mapping.get(n - 1, 0) else 0

            if depth > 0:
                requiredInv = mapping.get(depth - 1, inversionCount)
                if inversionCount != requiredInv:
                    return 0

            totalCount = 0
            for currentNum in range(n):
                if (usedMask & (1 << currentNum)) == 0:
                    newInversions = inversionCount
                    for nextIndex in range(currentNum + 1, n):
                        if (usedMask & (1 << nextIndex)) != 0:
                            newInversions += 1
                    totalCount = (totalCount + count_permutations(depth + 1, newInversions, usedMask | (1 << currentNum))) % M
            return totalCount

        return count_permutations(0, 0, 0)