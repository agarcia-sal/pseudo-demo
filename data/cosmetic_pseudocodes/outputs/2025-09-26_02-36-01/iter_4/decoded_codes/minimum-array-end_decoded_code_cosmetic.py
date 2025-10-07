class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(maxAllowed: int) -> bool:
            tempVar = x
            tally = 1
            while tempVar < maxAllowed:
                tempVar += 1
                if (tempVar & x) == x:
                    tally += 1
                    if tally == n:
                        return True
            return tally == n

        lowerBound = x
        upperBound = 2 * 10**7  # 2 * 10^7 as per pseudocode

        while lowerBound < upperBound:
            middleValue = (lowerBound + upperBound) // 2
            if canConstruct(middleValue):
                upperBound = middleValue
            else:
                lowerBound += 1

        return lowerBound