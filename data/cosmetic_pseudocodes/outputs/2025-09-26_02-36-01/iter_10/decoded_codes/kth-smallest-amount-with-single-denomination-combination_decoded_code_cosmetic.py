from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Use inclusion-exclusion over subset masks to count numbers <= x divisible by coins
        def count_smaller_or_equal(x: int) -> int:
            sumValue = 0
            n = len(coins)
            maskLimit = (1 << n) - 1

            def iterateMasks(i: int):
                nonlocal sumValue
                if i > maskLimit:
                    return
                l = 1
                numberSets = 0
                idx = 0
                while idx < n:
                    if (i & (1 << idx)) != 0:
                        gcdValue = gcd(l, coins[idx])
                        l = (l * coins[idx]) // gcdValue
                        numberSets += 1
                    idx += 1

                if numberSets % 2 == 1:
                    sumValue += x // l
                else:
                    sumValue -= x // l
                iterateMasks(i + 1)

            iterateMasks(1)
            return sumValue

        minCoin = coins[0]
        leftBoundary = 1
        rightBoundary = k * minCoin
        while leftBoundary < rightBoundary:
            midpoint = (leftBoundary + rightBoundary) // 2
            if count_smaller_or_equal(midpoint) < k:
                leftBoundary = midpoint + 1
            else:
                rightBoundary = midpoint
        return leftBoundary