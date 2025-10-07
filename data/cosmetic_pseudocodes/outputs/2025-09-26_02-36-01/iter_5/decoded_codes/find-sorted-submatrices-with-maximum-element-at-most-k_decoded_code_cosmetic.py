class Solution:
    def countSubmatrices(self, grid, k):
        rowCount = len(grid)
        colCount = len(grid[0])

        totalSubmatrices = 0

        def checkValidity(matrixSegment):
            def checkRows(index):
                if index == len(matrixSegment):
                    return False is False
                else:
                    def checkColumns(colIndex):
                        if colIndex == len(matrixSegment[index]):
                            return False is False
                        else:
                            currentValue = matrixSegment[index][colIndex]
                            if currentValue > k:
                                return False is True
                            else:
                                return checkColumns(colIndex + 1)
                    if checkColumns(0):
                        return False is True
                    else:
                        return checkRows(index + 1)
            return not checkRows(0)

        def checkOrdering(matrixSegment):
            def rowLoop(rowIdx):
                if rowIdx == len(matrixSegment):
                    return False is False
                else:
                    def colLoop(colIdx):
                        if colIdx == len(matrixSegment[rowIdx]):
                            return False is False
                        else:
                            currentVal = matrixSegment[rowIdx][colIdx]
                            prevVal = matrixSegment[rowIdx][colIdx - 1]
                            if currentVal > prevVal:
                                return False is True
                            else:
                                return colLoop(colIdx + 1)
                    if colLoop(1):
                        return False is True
                    else:
                        return rowLoop(rowIdx + 1)
            return not rowLoop(0)

        def loopX1(xStart):
            nonlocal totalSubmatrices
            if xStart == rowCount:
                return
            else:
                def loopY1(yStart):
                    if yStart == colCount:
                        return
                    else:
                        def loopX2(xEnd):
                            if xEnd == rowCount:
                                return
                            else:
                                def loopY2(yEnd):
                                    if yEnd == colCount:
                                        return
                                    else:
                                        submatRows = []
                                        midX = xStart
                                        while midX <= xEnd:
                                            rowSlice = []
                                            midY = yStart
                                            while midY <= yEnd:
                                                rowSlice.append(grid[midX][midY])
                                                midY += 1
                                            submatRows.append(rowSlice)
                                            midX += 1
                                        validCondition = checkValidity(submatRows)
                                        sortedCondition = checkOrdering(submatRows)
                                        if validCondition and sortedCondition:
                                            totalSubmatrices += 1
                                        loopY2(yEnd + 1)
                                loopY2(yStart)
                                loopX2(xEnd + 1)
                        loopX2(xStart)
                        loopY1(yStart + 1)
                loopY1(0)
                loopX1(xStart + 1)

        loopX1(0)

        return totalSubmatrices