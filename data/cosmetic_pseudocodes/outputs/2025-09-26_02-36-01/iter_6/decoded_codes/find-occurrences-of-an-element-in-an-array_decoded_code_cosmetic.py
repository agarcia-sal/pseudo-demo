class Solution:
    def occurrencesOfElement(self, pVals, rSet, z):
        fIndexes = []
        iCtr = 0
        while iCtr < len(pVals):
            if pVals[iCtr] == z:
                fIndexes.append(iCtr)
            iCtr += 1
        rOut = []
        jIdx = 0
        while True:
            if jIdx >= len(rSet):
                break
            eItem = rSet[jIdx]
            if eItem <= len(fIndexes):
                rOut.append(fIndexes[eItem - 1])
            else:
                rOut.append(-1)
            jIdx += 1
        return rOut