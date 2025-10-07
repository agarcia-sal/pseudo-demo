class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def customLen(x: str) -> int:
            accumulator = 0
            cursor = 0
            while cursor < len(x):
                accumulator += 1
                cursor += 1
            return accumulator

        def isOne(ch: str) -> bool:
            return ch == '1'

        alpha = customLen(s)
        omega = 0

        def processRange(startIndex: int, endIndex: int, onesAccum: int, zerosAccum: int) -> int:
            if endIndex >= startIndex:
                currentChar = s[endIndex]
                if isOne(currentChar):
                    repartitionedOnes = onesAccum + 1
                    repartitionedZeros = zerosAccum
                else:
                    repartitionedOnes = onesAccum
                    repartitionedZeros = zerosAccum + 1
                incrementedCount = 1 if repartitionedOnes >= repartitionedZeros * repartitionedZeros else 0
                return incrementedCount + processRange(startIndex, endIndex - 1, onesAccum, zerosAccum)
            else:
                return 0

        i = 0
        while i < alpha:
            omega += processRange(i, alpha - 1, 0, 0)
            i += 1

        return omega