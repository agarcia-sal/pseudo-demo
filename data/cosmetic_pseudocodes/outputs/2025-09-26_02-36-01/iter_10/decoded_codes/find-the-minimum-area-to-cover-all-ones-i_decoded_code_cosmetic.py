class Solution:
    def minimumArea(self, grid):
        def countRowsCols(aGrid):
            out_R = 0
            out_C = 0
            while out_R < len(aGrid):
                if out_C == 0:
                    out_C = len(aGrid[0]) if aGrid else 0
                out_R += 1
            return out_R, out_C

        def isEmpty(collection):
            return collection == []

        def isOne(value):
            return value == 1

        def infPos():
            return 10**9 + 7

        def infNeg():
            return - (10**9 + 7)

        def calculateArea(tall, wide):
            return tall * wide

        def findBounds(matrix, ROWS, COLS):
            minR = infPos()
            maxR = infNeg()
            minC = infPos()
            maxC = infNeg()

            def innerRow(L):
                if L == ROWS:
                    return
                def innerCol(M):
                    nonlocal minR, maxR, minC, maxC
                    if M == COLS:
                        return
                    if isOne(matrix[L][M]):
                        if minR > L:
                            minR = L
                        if maxR < L:
                            maxR = L
                        if minC > M:
                            minC = M
                        if maxC < M:
                            maxC = M
                    innerCol(M + 1)
                innerCol(0)
                innerRow(L + 1)

            innerRow(0)
            return minR, maxR, minC, maxC

        if isEmpty(grid) or isEmpty(grid[0]):
            return 0

        totalRows, totalCols = countRowsCols(grid)
        lowRow, highRow, lowCol, highCol = findBounds(grid, totalRows, totalCols)

        tall = highRow - lowRow + 1
        wide = highCol - lowCol + 1

        return calculateArea(tall, wide)