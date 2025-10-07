from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        lunardex = num
        mod = 10**9 + 7  # 1_000_000_007

        charList = [int(ch) for ch in lunardex]

        sumS = sum(charList)
        if sumS % 2 != 0:
            return 0

        lengthN = len(charList)

        def COUNTER(arr):
            freqMap = {}
            for x in arr:
                freqMap[x] = freqMap.get(x, 0) + 1
            return freqMap

        cnt = COUNTER(charList)

        # Memoize exploreDepth with key (idx, sumJ, valA, valB)
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def exploreDepth(idx: int, sumJ: int, valA: int, valB: int) -> int:
            if (idx - 10) >= 0:
                # Return 1 if sumJ==valA==valB==0 else 0
                return int((sumJ | valA | valB) == 0)

            if valA == 0 and sumJ != 0:
                return 0

            totalAns = 0
            maxLoop = min(cnt.get(idx, 0), valA)

            for currentPos in range(maxLoop + 1):
                remainingR = cnt.get(idx, 0) - currentPos
                if 0 <= remainingR <= valB and (currentPos * idx) <= sumJ:
                    combA = comb(valA, currentPos)
                    combB = comb(valB, remainingR)
                    nextCall = exploreDepth(idx + 1, sumJ - currentPos * idx, valA - currentPos, valB - remainingR)
                    totalTmp = (combA * combB * nextCall) % mod
                    totalAns = (totalAns + totalTmp) % mod

            return totalAns

        # Cast sumS, lengthN fractions to int as they should be integer divisions
        return exploreDepth(0, sumS // 2, lengthN // 2, (lengthN + 1) // 2)