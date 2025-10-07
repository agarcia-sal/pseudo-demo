class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            totalGroups = 0
            consecutiveLength = 0
            pos = 0
            n = len(s)
            while True:
                if pos >= n:
                    break

                consecutiveLength += 1

                if pos == n - 1 or s[pos] != s[pos + 1]:
                    totalGroups += ((consecutiveLength - 1) // m) + 1
                    if totalGroups > numOps:
                        return False
                    consecutiveLength = 0

                pos += 1

            return totalGroups <= numOps

        strLength = len(s)
        lowBound = 1
        highBound = strLength
        result = highBound

        while lowBound < highBound:
            midpoint = lowBound + ((highBound - lowBound) // 2)
            if check(midpoint):
                result = midpoint
                highBound = midpoint
            else:
                lowBound = midpoint + 1

        return lowBound