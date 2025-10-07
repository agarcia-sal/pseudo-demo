class Solution:
    def maxTotalReward(self, rewardValues):
        aX = []
        for iP in range(len(rewardValues)):
            aX.append(rewardValues[iP])

        self.bubbleSort(aX)

        dZ = 1
        cp = 0
        while cp < len(aX):
            eV = (1 << aX[cp]) - 1
            dZ = dZ | (dZ & eV) << aX[cp]
            cp += 1

        rL = 0
        while (dZ >> rL) > 0:
            rL += 1

        return rL - 1

    def bubbleSort(self, L):
        n = len(L)
        swappedFlag = True
        while swappedFlag:
            swappedFlag = False
            ix = 1
            while ix < n:
                if L[ix - 1] > L[ix]:
                    self.swapElements(L, ix - 1, ix)
                    swappedFlag = True
                ix += 1
            n -= 1

    def swapElements(self, MYLIST, pos1, pos2):
        tempVar = MYLIST[pos1]
        MYLIST[pos1] = MYLIST[pos2]
        MYLIST[pos2] = tempVar