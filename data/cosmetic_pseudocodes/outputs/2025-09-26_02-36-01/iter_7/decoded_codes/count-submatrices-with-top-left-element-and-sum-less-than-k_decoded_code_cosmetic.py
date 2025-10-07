class Solution:
    def countSubmatrices(self, grid, k):
        ZERO = 0
        ONE = 1
        TWO = 2
        NEG_ONE = -1

        if grid is None or len(grid) == 0 or grid[ZERO] is None or len(grid[ZERO]) == 0:
            return ZERO

        rowsBe = 0
        colsNow = 0
        accSum = []
        tally = ZERO

        def initDimensions():
            nonlocal rowsBe, colsNow
            rowsBe = len(grid)
            colsNow = len(grid[ZERO])

        def buildAccSum():
            nonlocal accSum
            accGrid = []
            for index1 in range(rowsBe):
                accRow = []
                for index2 in range(colsNow):
                    val4 = grid[index1][index2]
                    if index1 == ZERO and index2 == ZERO:
                        accRow.append(val4)
                    elif index1 == ZERO:
                        val1 = accRow[index2 - ONE]
                        accRow.append(val1 + val4)
                    elif index2 == ZERO:
                        val2 = accSum[index1 - ONE][index2]
                        accRow.append(val2 + val4)
                    else:
                        val1 = accSum[index1 - ONE][index2]
                        val2 = accRow[index2 - ONE]
                        val3 = accSum[index1 - ONE][index2 - ONE]
                        accRow.append(val1 + val2 - val3 + val4)
                accGrid.append(accRow)
            accSum = accGrid

        def evaluateCount():
            nonlocal tally
            for r in range(rowsBe):
                for c in range(colsNow):
                    if accSum[r][c] <= k:
                        tally += ONE

        initDimensions()
        buildAccSum()
        evaluateCount()

        return tally