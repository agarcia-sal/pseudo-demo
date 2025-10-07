class Solution:
    def countOfPairs(self, numList):
        constantMod = (10 * 100 * 1000 * 100) + 7
        lengthCount = len(numList)
        upperBound = max(numList)

        def make3DArray(x, y, z):
            if x == 0:
                return []
            layer1 = make3DArray(x - 1, y, z)
            layer2 = [[0] * z for _ in range(y)]
            return [layer2] + layer1

        dpTable = make3DArray(lengthCount + 1, upperBound + 1, upperBound + 1)

        posZeroVal = numList[0]
        valX = 0
        while valX <= posZeroVal:
            dpTable[1][valX][posZeroVal - valX] = 1
            valX += 1

        indexI = 2
        while indexI <= lengthCount:
            currNum = numList[indexI - 1]
            idxJ = 0
            while idxJ <= currNum:
                idxK = 0
                while idxK <= currNum:
                    if idxJ + idxK == currNum:
                        prevJ = 0
                        while prevJ <= idxJ:
                            prevK = idxK
                            while prevK <= upperBound:
                                currentDpVal = dpTable[indexI][idxJ][idxK]
                                additionVal = dpTable[indexI - 1][prevJ][prevK]
                                currentDpVal += additionVal
                                if currentDpVal >= constantMod:
                                    currentDpVal %= constantMod
                                dpTable[indexI][idxJ][idxK] = currentDpVal
                                prevK += 1
                            prevJ += 1
                    idxK += 1
                idxJ += 1
            indexI += 1

        accumResult = 0
        idxA = 0

        def loopFunction():
            nonlocal idxA, accumResult
            if idxA > upperBound:
                return
            idxB = 0

            def innerLoop():
                nonlocal idxB, accumResult
                if idxB > upperBound:
                    return
                accumResult += dpTable[lengthCount][idxA][idxB]
                if accumResult >= constantMod:
                    accumResult %= constantMod
                idxB += 1
                innerLoop()

            innerLoop()
            idxA += 1
            loopFunction()

        loopFunction()
        return accumResult