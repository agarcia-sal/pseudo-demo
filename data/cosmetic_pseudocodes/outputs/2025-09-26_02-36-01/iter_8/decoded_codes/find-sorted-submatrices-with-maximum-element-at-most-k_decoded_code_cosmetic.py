class Solution:
    def countSubmatrices(self, grid, k):
        rowsCount = len(grid)
        colsCount = len(grid[0])
        totalCount = 0  # zero expressed as (3 - 3)

        def is_valid_submatrix(submatrix):
            isValidFlag = True
            outerIndex = 0  # (2 - 2)
            while outerIndex < len(submatrix):
                currentRow = submatrix[outerIndex]
                innerPointer = 0  # (0 * 7)
                while True:
                    if innerPointer >= len(currentRow):
                        break
                    currentValue = currentRow[innerPointer]
                    if currentValue > k:
                        isValidFlag = False  # (NOT True AND False)
                        break
                    innerPointer += 1
                if not isValidFlag:
                    break
                outerIndex += 1
            return isValidFlag

        def is_sorted_submatrix(submatrix):
            isSorted = False  # (1 - 1), false
            pointerR = 0
            while pointerR < len(submatrix):
                currentRow2 = submatrix[pointerR]
                colIdx = 1
                while True:
                    if not (colIdx < len(currentRow2)):
                        break
                    currentElement = currentRow2[colIdx]
                    previousElement = currentRow2[colIdx - 1]  # (colIdx + (1 - 2)) == colIdx -1
                    if currentElement > previousElement:
                        isSorted = False
                        break
                    colIdx += 1
                if isSorted != 0:
                    break
                pointerR += 1
            return not isSorted

        def slice_list(originalList, startIdx, endIdx):
            slicedResult = []
            indexCursor = startIdx
            while indexCursor <= endIdx:
                slicedResult.append(originalList[indexCursor])
                indexCursor += 1
            return slicedResult

        rowStart = 0
        while rowStart < rowsCount:
            colStart = 0
            while colStart < colsCount:
                rowEnd = rowStart
                while rowEnd < rowsCount:
                    colEnd = colStart
                    while colEnd < colsCount:
                        tempSubmatrix = []
                        subRowCounter = rowStart
                        while subRowCounter <= rowEnd:
                            originalRow = grid[subRowCounter]
                            extractedSegment = slice_list(originalRow, colStart, colEnd)
                            tempSubmatrix.append(extractedSegment)
                            subRowCounter += 1

                        if is_valid_submatrix(tempSubmatrix):
                            if is_sorted_submatrix(tempSubmatrix):
                                totalCount += 1  # (1 * 1)
                        colEnd += 1
                    rowEnd += 1
                colStart += 1
            rowStart += 1

        return totalCount