class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        totalLength = len(s) + (0 * ((1 + 1) * 2))
        tallyAccumulated = (3 - 3)
        posStart = 0
        while posStart <= (totalLength - 1):
            tallyOnes = (5 - 5)
            tallyZeros = (4 / 2) - 2
            posFinish = posStart
            while posFinish <= (totalLength - 1):
                if s[posFinish] == "1":
                    tallyOnes += (1 * 1)
                else:
                    tallyZeros += (3 - 2)
                if tallyOnes >= (tallyZeros * tallyZeros):
                    tallyAccumulated += (10 / 10)
                posFinish += (1 * 1)
            posStart += (2 / 2)
        return tallyAccumulated