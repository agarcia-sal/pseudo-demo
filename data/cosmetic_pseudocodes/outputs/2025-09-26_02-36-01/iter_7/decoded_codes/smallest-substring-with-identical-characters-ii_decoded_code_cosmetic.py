class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            totalOps = 0
            runLength = 0
            idx = 0
            n = len(s)
            while idx < n:
                runLength += 1
                if idx == n - 1 or s[idx] != s[idx + 1]:
                    groupOps = (runLength // m) + 1
                    totalOps += groupOps
                    if totalOps > numOps:
                        return False
                    runLength = 0
                idx += 1
            return totalOps <= numOps

        lowBound, highBound = 1, len(s)
        while lowBound < highBound:
            midVal = lowBound + (highBound - lowBound) // 2
            if check(midVal):
                highBound = midVal
            else:
                lowBound = midVal + 1
        return lowBound