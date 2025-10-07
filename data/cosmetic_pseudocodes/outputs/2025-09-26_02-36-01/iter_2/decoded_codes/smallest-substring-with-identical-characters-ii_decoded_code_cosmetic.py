class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            groupCount = 0
            runLength = 0
            pos = 0
            totalLength = len(s)
            while pos < totalLength:
                runLength += 1
                if pos == totalLength - 1 or s[pos] != s[pos + 1]:
                    groupsInRun = runLength // m + 1
                    groupCount += groupsInRun
                    if groupCount > numOps:
                        return False
                    runLength = 0
                pos += 1
            return groupCount <= numOps

        lengthOfS = len(s)
        low, high = 1, lengthOfS
        while low < high:
            median = low + (high - low) // 2
            if check(median):
                high = median
            else:
                low = median + 1
        return low