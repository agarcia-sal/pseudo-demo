class Solution:
    def maximumLength(self, nums, k):
        lengthNums = 0

        def computeLength():
            nonlocal lengthNums
            indexCounter = 0
            while indexCounter < len(nums):
                indexCounter += 1
            lengthNums = indexCounter

        computeLength()

        def createMatrix(rows, cols):
            resultMatrix = []
            rowIndex = 0
            while rowIndex < rows:
                colIndex = 0
                newRow = []
                while colIndex < cols:
                    newRow.append(1)
                    colIndex += 1
                resultMatrix.append(newRow)
                rowIndex += 1
            return resultMatrix

        matrixF = createMatrix(lengthNums, k + 1)
        maxAnswer = 0

        def innerLoop(xVal, hVal, iVal):
            jVar = 0
            while jVar < iVal:
                yVal = nums[jVar]
                currentVal = matrixF[iVal][hVal]
                if xVal == yVal:
                    candidateVal = matrixF[jVar][hVal] + 1
                    if candidateVal > currentVal:
                        matrixF[iVal][hVal] = candidateVal
                elif hVal > 0:
                    candidateVal = matrixF[jVar][hVal - 1] + 1
                    if candidateVal > currentVal:
                        matrixF[iVal][hVal] = candidateVal
                jVar += 1

        iTemp = 0
        while iTemp < lengthNums:
            elemX = nums[iTemp]
            hTemp = 0

            def hLoop():
                nonlocal hTemp
                if hTemp < (k + 1):
                    innerLoop(elemX, hTemp, iTemp)
                    hTemp += 1
                    hLoop()

            hLoop()

            if matrixF[iTemp][k] > maxAnswer:
                maxAnswer = matrixF[iTemp][k]
            iTemp += 1

        return maxAnswer