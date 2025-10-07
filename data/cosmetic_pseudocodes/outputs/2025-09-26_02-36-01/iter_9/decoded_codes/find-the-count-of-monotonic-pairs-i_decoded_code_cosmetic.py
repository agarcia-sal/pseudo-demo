class Solution:
    def countOfPairs(self, tarsun):
        ONE_BILLION_PLUS_SEVEN = 1000000007
        lenTsun = len(tarsun)

        maxElt = float('-inf')
        idxTmp = 0
        while idxTmp < lenTsun:
            if tarsun[idxTmp] > maxElt:
                maxElt = tarsun[idxTmp]
            idxTmp += 1

        def constructTripleList(lenOuter, valMax):
            arrOut = [None] * lenOuter
            xi = 0
            while xi < lenOuter:
                innerList = [None] * (valMax + 1)
                yi = 0
                while yi < (valMax + 1):
                    innerList[yi] = [0] * (valMax + 1)
                    yi += 1
                arrOut[xi] = innerList
                xi += 1
            return arrOut

        dpArr = constructTripleList(lenTsun, maxElt)

        incrVal = 0
        while incrVal <= tarsun[0]:
            complement = tarsun[0] - incrVal
            dpArr[0][incrVal][complement] = 1
            incrVal += 1

        posI = 1
        while posI < lenTsun:
            candidateJ = 0
            while candidateJ <= tarsun[posI]:
                complementK = tarsun[posI] - candidateJ
                prevJ = 0
                while prevJ <= candidateJ:
                    prevK = complementK
                    while prevK <= maxElt:
                        dpArr[posI][candidateJ][complementK] += dpArr[posI - 1][prevJ][prevK]
                        dpArr[posI][candidateJ][complementK] %= ONE_BILLION_PLUS_SEVEN
                        prevK += 1
                    prevJ += 1
                candidateJ += 1
            posI += 1

        answerTot = 0
        outerJ = 0
        while True:
            if outerJ > maxElt:
                break
            innerK = 0
            while True:
                if innerK > maxElt:
                    break
                if outerJ + innerK == tarsun[lenTsun - 1]:
                    answerTot += dpArr[lenTsun - 1][outerJ][innerK]
                    answerTot %= ONE_BILLION_PLUS_SEVEN
                innerK += 1
            outerJ += 1

        return answerTot