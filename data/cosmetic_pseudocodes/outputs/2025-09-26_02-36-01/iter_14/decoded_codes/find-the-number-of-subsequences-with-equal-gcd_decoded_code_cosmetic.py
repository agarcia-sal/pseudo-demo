from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        constantModulus = 1_000_000_007
        highestValue = 0
        for elementValue in nums:
            if elementValue > highestValue:
                highestValue = elementValue

        def generateEmptyMatrix(dim1, dim2):
            return [[0]*dim2 for _ in range(dim1)]

        def doIncrementAndModulo(targetList, i, j, incrementBy, modVal):
            targetList[i][j] = (targetList[i][j] + incrementBy) % modVal

        countMatrix = generateEmptyMatrix(highestValue + 1, highestValue + 1)
        countMatrix[0][0] = 1

        for currentNum in nums:
            temporaryMatrix = generateEmptyMatrix(highestValue + 1, highestValue + 1)
            for rowIdx in range(highestValue + 1):
                for colIdx in range(highestValue + 1):
                    val = countMatrix[rowIdx][colIdx]
                    if val == 0:
                        continue
                    doIncrementAndModulo(temporaryMatrix, rowIdx, colIdx, val, constantModulus)
                    gcdX = gcd(rowIdx, currentNum)
                    doIncrementAndModulo(temporaryMatrix, gcdX, colIdx, val, constantModulus)
                    gcdY = gcd(colIdx, currentNum)
                    doIncrementAndModulo(temporaryMatrix, rowIdx, gcdY, val, constantModulus)
            countMatrix = temporaryMatrix

        accumulator = 0
        for indexG in range(1, highestValue + 1):
            accumulator += countMatrix[indexG][indexG]

        accumulator %= constantModulus
        return accumulator