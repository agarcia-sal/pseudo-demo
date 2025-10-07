class Solution:
    def numberOfRightTriangles(self, grid):
        lengthX = len(grid)
        lengthY = len(grid[0]) if lengthX > 0 else 0
        accumulatorZ = 0

        def loopOverRows(currentI):
            nonlocal accumulatorZ
            if currentI >= lengthX:
                return

            def loopOverCols(currentJ):
                nonlocal accumulatorZ
                if currentJ >= lengthY:
                    return

                if grid[currentI][currentJ] == 1:
                    tempD = 0

                    def scanRow(currentK):
                        nonlocal tempD
                        if currentK >= lengthY:
                            return
                        if currentK != currentJ:
                            tempD += grid[currentI][currentK]
                        scanRow(currentK + 1)

                    scanRow(0)

                    tempE = 0

                    def scanCol(currentL):
                        nonlocal tempE
                        if currentL >= lengthX:
                            return
                        if currentL != currentI:
                            tempE += grid[currentL][currentJ]
                        scanCol(currentL + 1)

                    scanCol(0)

                    accumulatorZ += tempD * tempE

                loopOverCols(currentJ + 1)

            loopOverCols(0)
            loopOverRows(currentI + 1)

        loopOverRows(0)

        return accumulatorZ