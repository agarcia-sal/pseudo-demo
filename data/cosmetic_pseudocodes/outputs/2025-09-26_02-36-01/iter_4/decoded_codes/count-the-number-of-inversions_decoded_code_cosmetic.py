class Solution:
    def numberOfPermutations(self, n, requirements):
        MODULO = 10**9 + 7
        requirementMap = {}
        for key, value in requirements:
            requirementMap[key] = value

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(prefixLen, inversionCount, usedMask):
            if prefixLen == n:
                requiredInversion = requirementMap.get(n - 1, 0)
                return 1 if inversionCount == requiredInversion else 0

            if prefixLen > 0:
                expectedInv = requirementMap.get(prefixLen - 1, inversionCount)
                if inversionCount != expectedInv:
                    return 0

            totalCount = 0
            for candidate in range(n):
                bit_at_candidate = 1 << candidate
                if (usedMask & bit_at_candidate) == 0:
                    inversionNext = inversionCount
                    for j in range(candidate + 1, n):
                        bit_at_j = 1 << j
                        if (usedMask & bit_at_j) != 0:
                            inversionNext += 1
                    newUsedMask = usedMask | bit_at_candidate
                    totalCount = (totalCount + count_permutations(prefixLen + 1, inversionNext, newUsedMask)) % MODULO

            return totalCount

        return count_permutations(0, 0, 0)