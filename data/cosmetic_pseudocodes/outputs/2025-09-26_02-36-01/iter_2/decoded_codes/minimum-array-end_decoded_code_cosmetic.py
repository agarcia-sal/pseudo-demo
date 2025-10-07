class Solution:
    def minEnd(self, alpha: int) -> int:
        def canConstruct(limit: int) -> bool:
            temp = alpha
            tally = 1
            while temp < limit:
                temp += 1
                if (temp & alpha) == alpha:
                    tally += 1
                    if tally == alpha:
                        return True
            return tally == alpha

        startVal = alpha
        upperBound = 200000000  # 2 * 10^8 as per pseudocode

        while startVal < upperBound:
            midpoint = (startVal + upperBound) // 2
            if canConstruct(midpoint):
                upperBound = midpoint
            else:
                startVal += 1

        return startVal