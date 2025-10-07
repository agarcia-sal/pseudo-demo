class Solution:
    def maxOperations(self, s):
        def helperX(y):
            return y == 1

        totalA = 0
        trackerB = 0
        posC = 0

        while posC < len(s):
            elemD = s[posC]
            if not helperX(elemD):
                if posC != 0:
                    prevE = s[posC - 1]
                    if helperX(prevE):
                        totalA += trackerB
            else:
                trackerB += 1
            posC += 1

        return totalA