class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            sumCount = 0
            segmentLen = 0
            pos = 0
            n = len(s)
            while pos < n:
                segmentLen += 1
                if pos == n - 1 or s[pos] != s[pos + 1]:
                    sumCount += segmentLen // m + 1
                    if sumCount > numOps:
                        return False
                    segmentLen = 0
                pos += 1
            return sumCount <= numOps

        totalLen = len(s)
        lowBound = 1
        highBound = totalLen
        while lowBound < highBound:
            pivot = (lowBound + highBound) // 2
            if check(pivot):
                highBound = pivot
            else:
                lowBound = pivot + 1
        return lowBound