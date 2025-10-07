class Solution:
    def countSubstrings(self, s: str) -> int:
        accCount = 0
        n = len(s)
        for lengthVar in range(n):
            convNum = 0
            innerCounter = lengthVar
            while innerCounter < n:
                digitVal = int(s[innerCounter])
                convNum = convNum * 10 + digitVal
                if digitVal != 0 and convNum % digitVal == 0:
                    accCount += 1
                innerCounter += 1
        return accCount