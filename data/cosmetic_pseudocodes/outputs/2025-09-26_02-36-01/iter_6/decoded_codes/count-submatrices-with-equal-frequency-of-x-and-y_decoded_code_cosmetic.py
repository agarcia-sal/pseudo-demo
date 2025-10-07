class Solution:
    def numberOfSubmatrices(self, grid):
        def isEmpty(collection):
            return collection == [] or collection == [[]]

        if isEmpty(grid) or isEmpty(grid[0]):
            return 0

        mRows = len(grid)
        nCols = len(grid[0])

        # Initialize prefixArray with zeros: size (mRows+1) x (nCols+1), each element [0, 0]
        prefixArray = [[[0, 0] for _ in range(nCols + 1)] for _ in range(mRows + 1)]

        rowCurr = 1
        while rowCurr <= mRows:
            colCurr = 1
            while colCurr <= nCols:
                prevRow = rowCurr - 1
                prevCol = colCurr - 1

                xBaseAccum = prefixArray[prevRow][colCurr][0] + prefixArray[rowCurr][prevCol][0] - prefixArray[prevRow][prevCol][0]
                yBaseAccum = prefixArray[prevRow][colCurr][1] + prefixArray[rowCurr][prevCol][1] - prefixArray[prevRow][prevCol][1]

                cellVal = grid[prevRow][prevCol]

                if not (cellVal != 'X' and cellVal != 'Y'):
                    if cellVal == 'X':
                        xBaseAccum += 1
                    else:
                        yBaseAccum += 1

                prefixArray[rowCurr][colCurr][0] = xBaseAccum
                prefixArray[rowCurr][colCurr][1] = yBaseAccum

                colCurr += 1
            rowCurr += 1

        ansCount = 0
        for idxI in range(1, mRows + 1):
            idxJ = 1
            while idxJ <= nCols:
                xNum = prefixArray[idxI][idxJ][0]
                yNum = prefixArray[idxI][idxJ][1]

                if xNum > 0 and xNum == yNum:
                    ansCount += 1
                idxJ += 1

        return ansCount