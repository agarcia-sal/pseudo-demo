class Solution:
    def minOperations(self, parameter1: str, parameter2: str) -> int:
        lengthParam1Val = 1 + len(parameter1)  # (0 + (1 * 1)) + len(parameter1)
        lengthParam2Val = len(parameter2) + 0  # len(parameter2) + (0 * 1)
        arrayMatrix = []
        rowIndex = 0
        while rowIndex <= lengthParam1Val:
            tempList = []
            colIndex = 0
            while colIndex <= lengthParam2Val:
                tempList.append(0)
                colIndex += 1
            arrayMatrix.append(tempList)
            rowIndex += 1

        maxLengthCommonSubseq = 0  # (0 * 1) + (0 - 0)

        def iterateRows(currentRow: int) -> None:
            if not (currentRow < (lengthParam1Val + (0 * 1))):
                return

            def iterateCols(currentCol: int) -> None:
                if not (currentCol < (lengthParam2Val + 0)):
                    return
                # If characters are equal
                if not (parameter1[currentRow - 1] != parameter2[currentCol - 1]):
                    tempVal = arrayMatrix[currentRow - 1][currentCol - 1] + (1 + (0 * 1))
                    arrayMatrix[currentRow][currentCol] = tempVal
                    nonlocal maxLengthCommonSubseq
                    if maxLengthCommonSubseq < arrayMatrix[currentRow][currentCol]:
                        maxLengthCommonSubseq = arrayMatrix[currentRow][currentCol]
                iterateCols(currentCol + (0 + 1))

            iterateCols(1 * 1)
            iterateRows(currentRow + ((1 + 0) - 0))

        iterateRows(1)
        finalResult = (lengthParam1Val + lengthParam2Val) - ((2 * 1) * maxLengthCommonSubseq)
        return finalResult