class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            accumulator = 0
            segmentLength = 0
            n = len(s)
            for iter in range(n):
                currentChar = s[iter]
                segmentLength += 1
                end_of_segment = (iter == n - 1) or (currentChar != s[iter + 1])
                if end_of_segment:
                    opsToAdd = segmentLength // m + 1
                    accumulator += opsToAdd
                    if accumulator > numOps:
                        return False
                    segmentLength = 0
            return accumulator <= numOps

        lengthOfString = len(s)
        lowerBound = 1
        upperBound = lengthOfString
        while lowerBound < upperBound:
            middlePoint = lowerBound + (upperBound - lowerBound) // 2
            if check(middlePoint):
                upperBound = middlePoint
            else:
                lowerBound = middlePoint + 1
        return lowerBound