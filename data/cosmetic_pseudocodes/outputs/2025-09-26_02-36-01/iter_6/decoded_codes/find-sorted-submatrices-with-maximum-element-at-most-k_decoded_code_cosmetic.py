class Solution:
    def countSubmatrices(self, grid, k):
        totalRows = len(grid)
        totalCols = len(grid[0])
        accumulator = 0

        def checkValidity(matrixPart):
            def checkRows(indexRow):
                if not (indexRow < len(matrixPart)):
                    return True
                def checkCells(indexCol):
                    if not (indexCol < len(matrixPart[indexRow])):
                        return checkRows(indexRow + 1)
                    currentElement = matrixPart[indexRow][indexCol]
                    if currentElement > k:
                        return False
                    return checkCells(indexCol + 1)
                return checkCells(0)
            return checkRows(0)

        def checkSorted(matrixPart):
            def validateRow(rowIndex):
                if not (rowIndex < len(matrixPart)):
                    return True
                def validateCols(colIndex):
                    if not (colIndex < len(matrixPart[rowIndex]) - 1):
                        return validateRow(rowIndex + 1)
                    currentVal = matrixPart[rowIndex][colIndex + 1]
                    prevVal = matrixPart[rowIndex][colIndex]
                    if currentVal > prevVal:
                        return False
                    return validateCols(colIndex + 1)
                return validateCols(0)
            return validateRow(0)

        startX = 0
        while startX <= totalRows - 1:
            startY = 0
            while startY <= totalCols - 1:
                endX = startX
                while endX <= totalRows - 1:
                    endY = startY
                    while endY <= totalCols - 1:
                        collectedSubmatrix = []
                        def extractRows(rowPointer):
                            if not (rowPointer <= endX):
                                return
                            extractedRow = []
                            colPointer = startY
                            while colPointer <= endY:
                                tempElem = grid[rowPointer][colPointer]
                                extractedRow.append(tempElem)
                                colPointer += 1
                            collectedSubmatrix.append(extractedRow)
                            extractRows(rowPointer + 1)
                        extractRows(startX)
                        if checkValidity(collectedSubmatrix) and checkSorted(collectedSubmatrix):
                            accumulator += 1
                        endY += 1
                    endX += 1
                startY += 1
            startX += 1

        return accumulator