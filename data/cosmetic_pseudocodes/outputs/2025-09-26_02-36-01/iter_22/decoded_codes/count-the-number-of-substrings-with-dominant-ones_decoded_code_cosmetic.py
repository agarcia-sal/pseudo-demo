class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        totalLength = len(s)
        accumulator = 0
        indexA = 0
        while indexA <= totalLength - 1:
            sumOnes = 0
            sumZeros = 0
            indexB = indexA
            while indexB <= totalLength - 1:
                if s[indexB] == '1':
                    sumOnes += 1
                else:
                    sumZeros += 1
                if sumOnes >= (sumZeros * sumZeros):
                    accumulator += 1
                indexB += 1
            indexA += 1
        return accumulator