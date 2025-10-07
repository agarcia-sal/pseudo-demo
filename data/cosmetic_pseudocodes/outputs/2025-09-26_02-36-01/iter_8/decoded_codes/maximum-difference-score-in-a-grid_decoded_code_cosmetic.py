class Solution:
    def maxScore(self, grid):
        sizeRow = len(grid)
        sizeCol = len(grid[0])

        # auxInf and auxNegInf calculation mimicking original pseudocode bitwise ops
        auxInf = -((~0) + 1)
        auxNegInf = -((~0) - 1)
        infPlus = auxInf + auxNegInf

        # Initialize dpMatrix filled with infPlus
        dpMatrix = [[infPlus for _ in range(sizeCol)] for _ in range(sizeRow)]

        dpMatrix[0][0] = grid[0][0]
        maximumScore = auxNegInf

        # Fill first row of dpMatrix
        indexJ = 1
        while True:
            if indexJ >= sizeCol:
                break
            if dpMatrix[0][indexJ - 1] < grid[0][indexJ]:
                dpMatrix[0][indexJ] = dpMatrix[0][indexJ - 1]
            else:
                dpMatrix[0][indexJ] = grid[0][indexJ]
            indexJ += 1

        # Fill first column of dpMatrix
        indexI = 1
        while True:
            if indexI >= sizeRow:
                break
            if dpMatrix[indexI - 1][0] < grid[indexI][0]:
                dpMatrix[indexI][0] = dpMatrix[indexI - 1][0]
            else:
                dpMatrix[indexI][0] = grid[indexI][0]
            indexI += 1

        # Fill rest of dpMatrix and track maximumScore
        iterI = 1
        while iterI < sizeRow:
            iterJ = 1
            while iterJ < sizeCol:
                if dpMatrix[iterI][iterJ - 1] < dpMatrix[iterI - 1][iterJ]:
                    dpMatrix[iterI][iterJ] = dpMatrix[iterI][iterJ - 1]
                else:
                    dpMatrix[iterI][iterJ] = dpMatrix[iterI - 1][iterJ]

                tempScore = grid[iterI][iterJ] - dpMatrix[iterI][iterJ]
                if maximumScore < tempScore:
                    maximumScore = tempScore
                iterJ += 1
            iterI += 1

        return maximumScore