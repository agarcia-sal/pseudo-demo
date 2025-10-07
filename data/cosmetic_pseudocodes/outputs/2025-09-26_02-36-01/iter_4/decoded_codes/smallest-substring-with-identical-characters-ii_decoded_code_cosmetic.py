class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            totalSegments = 0
            segmentLength = 0
            position = 0
            strLength = len(s)
            while position < strLength:
                segmentLength += 1
                if position == strLength - 1 or s[position] != s[position + 1]:
                    segmentsForThisBlock = (segmentLength // m) + 1
                    totalSegments += segmentsForThisBlock
                    if totalSegments > numOps:
                        return False
                    segmentLength = 0
                position += 1
            return totalSegments <= numOps

        lengthOfS = len(s)
        lowBound = 1
        highBound = lengthOfS
        while lowBound < highBound:
            midPoint = lowBound + (highBound - lowBound) // 2
            if check(midPoint):
                highBound = midPoint
            else:
                lowBound = midPoint + 1
        return lowBound