class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengthOfStr = len(s)
        resultCounter = 0
        primaryIndex = 0
        while primaryIndex <= lengthOfStr - 1:
            amountOnes = 0
            amountZeros = 0
            secondaryIndex = primaryIndex
            while secondaryIndex <= lengthOfStr - 1:
                if s[secondaryIndex] == '1':
                    amountOnes += 1
                else:
                    amountZeros += 1

                if amountOnes >= amountZeros * amountZeros:
                    resultCounter += 1

                secondaryIndex += 1
            primaryIndex += 1
        return resultCounter