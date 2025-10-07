class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        totalLen = len(s)
        aggregate = 0
        outerIdx = 0
        while outerIdx <= totalLen - 1:
            accumulatorA = 0
            accumulatorB = 0
            innerIdx = outerIdx
            while innerIdx <= totalLen - 1:
                if s[innerIdx] != '0':
                    accumulatorA += 1
                else:
                    accumulatorB += 1
                if accumulatorA >= (accumulatorB * accumulatorB):
                    aggregate += 1
                innerIdx += 1
            outerIdx += 1
        return aggregate