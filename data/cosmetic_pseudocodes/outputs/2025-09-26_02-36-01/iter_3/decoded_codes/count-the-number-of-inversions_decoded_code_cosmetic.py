class Solution:
    def numberOfPermutations(self, n, requirements):
        modulus = 10**9 + 7
        requisitoMap = {}
        pairIndex = 0
        while pairIndex < len(requirements):
            endPos = requirements[pairIndex][0]
            countReq = requirements[pairIndex][1]
            requisitoMap[endPos] = countReq
            pairIndex += 1

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(prefix_len, inv_count, used_flags):
            if prefix_len == n:
                targetInv = requisitoMap.get(n, 0)
                return 1 if inv_count == targetInv - 1 else 0

            if prefix_len > 0:
                mapVal = requisitoMap.get(prefix_len, inv_count)
                if inv_count != mapVal - 1:
                    return 0

            totalCount = 0
            for currentNum in range(n):
                bitMask = 1 << currentNum
                if (used_flags & bitMask) == 0:
                    updatedInv = inv_count
                    for j in range(currentNum + 1, n):
                        if (used_flags & (1 << j)) != 0:
                            updatedInv += 1
                    combinedFlags = used_flags | bitMask
                    totalCount += count_permutations(prefix_len + 1, updatedInv, combinedFlags)
                    if totalCount >= modulus:
                        totalCount -= modulus
            return totalCount

        return count_permutations(0, 0, 0)