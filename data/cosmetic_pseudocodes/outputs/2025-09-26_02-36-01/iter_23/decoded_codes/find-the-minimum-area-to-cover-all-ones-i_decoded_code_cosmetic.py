from math import inf

class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        def traverseRows(indexRow, limitRow, curMinRow, curMaxRow, traverseColsProc):
            if indexRow > limitRow:
                traverseColsProc()
                return curMinRow, curMaxRow
            else:
                def traverseCols(indexCol, limitCol, curMinC, curMaxC, updatedMinR, updatedMaxR):
                    if indexCol > limitCol:
                        return updatedMinR, updatedMaxR, curMinC, curMaxC
                    else:
                        if grid[indexRow][indexCol] == 1:
                            updatedMinR = updatedMinR if updatedMinR < indexRow else indexRow
                            updatedMaxR = updatedMaxR if updatedMaxR > indexRow else indexRow
                            curMinC = curMinC if curMinC < indexCol else indexCol
                            curMaxC = curMaxC if curMaxC > indexCol else indexCol
                        return traverseCols(indexCol + 1, limitCol, curMinC, curMaxC, updatedMinR, updatedMaxR)

                newMinRow = curMinRow
                newMaxRow = curMaxRow

                colResult = traverseCols(0, len(grid[0]) - 1, inf, -inf, newMinRow, newMaxRow)
                newMinRow, newMaxRow, minColLocal, maxColLocal = colResult

                nextResult = traverseRows(indexRow + 1, limitRow, newMinRow, newMaxRow, lambda: ())
                return nextResult[0], nextResult[1], minColLocal, maxColLocal

        def findBounds():
            return traverseRows(0, len(grid) - 1, inf, -inf, lambda: ())

        minRowGlobal = inf
        maxRowGlobal = -inf
        minColGlobal = inf
        maxColGlobal = -inf

        def updateBounds(i, j, currMinRow, currMaxRow, currMinCol, currMaxCol):
            if i > len(grid) - 1:
                return currMinRow, currMaxRow, currMinCol, currMaxCol
            else:
                if j > len(grid[0]) - 1:
                    return updateBounds(i + 1, 0, currMinRow, currMaxRow, currMinCol, currMaxCol)
                else:
                    if grid[i][j] == 1:
                        currMinRow = currMinRow if currMinRow < i else i
                        currMaxRow = currMaxRow if currMaxRow > i else i
                        currMinCol = currMinCol if currMinCol < j else j
                        currMaxCol = currMaxCol if currMaxCol > j else j
                    return updateBounds(i, j + 1, currMinRow, currMaxRow, currMinCol, currMaxCol)

        minRowGlobal, maxRowGlobal, minColGlobal, maxColGlobal = updateBounds(
            0, 0, inf, -inf, inf, -inf)

        if minRowGlobal == inf:
            return 0
        else:
            heightVal = maxRowGlobal - minRowGlobal + 1
            widthVal = maxColGlobal - minColGlobal + 1
            return heightVal * widthVal