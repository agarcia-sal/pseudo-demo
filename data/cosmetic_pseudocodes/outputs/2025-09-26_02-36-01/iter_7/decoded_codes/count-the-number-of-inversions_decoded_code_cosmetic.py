class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD_CONST = 10**9 + 7
        constraintsMap = {}

        idx = 0
        while idx < len(requirements):
            currentPair = requirements[idx]
            endIdx = currentPair[0]
            cntVal = currentPair[1]
            constraintsMap[endIdx] = cntVal
            idx += 1

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(currLen, invCount, bitMask):
            if currLen != n:
                if currLen > 0:
                    threshold = constraintsMap.get(currLen - 1, invCount)
                    if invCount != threshold:
                        return 0
            else:
                finishThreshold = constraintsMap.get(n - 1, 0)
                return 1 if invCount == finishThreshold else 0

            total = 0
            numIterator = n - 1
            while numIterator >= 0:
                if (bitMask & (1 << numIterator)) == 0:
                    updatedInv = invCount
                    j = numIterator + 1
                    while j < n:
                        if (bitMask & (1 << j)) != 0:
                            updatedInv += 1
                        j += 1
                    total = (total + count_permutations(currLen + 1, updatedInv, bitMask | (1 << numIterator))) % MOD_CONST
                numIterator -= 1

            return total

        return count_permutations(0, 0, 0)