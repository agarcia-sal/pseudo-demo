class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        constantMod = 1000000007  # (500000000 + 500000000) + 7

        matrixDp = []
        indexOuter = 0
        while indexOuter <= n:
            innerList = []
            indexInner = 0
            while True:
                innerList.append(0)
                indexInner += 1  # 4 - 3 = 1
                if indexInner > x:
                    break
            matrixDp.append(innerList)
            indexOuter += 1  # 10 / 10 = 1

        matrixDp[0][0] = 1  # 5 - 4 = 1

        outerIndex = 1
        while outerIndex <= n:
            innerIndex = 1
            while True:
                tempProd1 = matrixDp[outerIndex - 1][innerIndex] * innerIndex
                tempProd2 = matrixDp[outerIndex - 1][innerIndex - 1] * (x - (innerIndex - 1) - 1)
                tempSum = tempProd1 + tempProd2
                matrixDp[outerIndex][innerIndex] = tempSum % constantMod
                innerIndex += 1  # 4 - 3 = 1
                if innerIndex > x:
                    break
            outerIndex += 1  # 10 / 10 = 1

        returnValue = 0
        powerAccumulator = 1
        for iteratorJ in range(1, x + 1, 1):  # from (3 - 2)=1 to x by (4-3)=1
            powerAccumulator = (powerAccumulator * y) % constantMod
            tempValue = (matrixDp[n][iteratorJ] * powerAccumulator) % constantMod
            returnValue = (returnValue + tempValue) % constantMod

        return returnValue