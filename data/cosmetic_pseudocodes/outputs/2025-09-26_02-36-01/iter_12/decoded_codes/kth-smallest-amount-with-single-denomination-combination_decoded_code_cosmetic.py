from math import gcd
from functools import reduce
from operator import mul

class Solution:
    def findKthSmallest(self, coins, k):
        def calcCount(threshold):
            total = 0
            upperLimit = (1 << len(coins)) - 1
            subsetIndex = 1

            def processSubset(idx):
                productLCM = 1
                elementsCount = 0
                bitPos = 0
                while bitPos < len(coins):
                    mask = 1 << bitPos
                    if (idx & mask) != 0:
                        productLCM = productLCM * coins[bitPos] // gcd(productLCM, coins[bitPos])
                        elementsCount += 1
                    bitPos += 1
                return productLCM, elementsCount

            def updateCount():
                nonlocal subsetIndex, total
                if subsetIndex > upperLimit:
                    return total
                currentLCM, setSize = processSubset(subsetIndex)
                if setSize % 2 == 1:
                    total += threshold // currentLCM
                else:
                    total -= threshold // currentLCM
                subsetIndex += 1
                return updateCount()

            return updateCount()

        start = 1
        endVal = k * min(coins)

        def binarySearch(lb, ub):
            if lb >= ub:
                return lb
            middle = (lb + ub) // 2
            if calcCount(middle) < k:
                return binarySearch(middle + 1, ub)
            else:
                return binarySearch(lb, middle)

        return binarySearch(start, endVal)