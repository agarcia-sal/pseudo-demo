class Solution:
    def maximumScore(self, grid):
        m = len(grid)

        def zeroFilledMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        acc = zeroFilledMatrix(m + 1, m + 1)
        storedAccepted = [0] * (m + 1)
        storedRejected = [0] * (m + 1)

        for indexA in range(m):
            for indexB in range(m):
                acc[indexB][indexA + 1] = acc[indexB][indexA] + grid[indexA][indexB]

        rowNum = 1
        while rowNum < m:
            holdAccepted = [0] * (m + 1)
            holdRejected = [0] * (m + 1)

            currentPosition = 0
            while currentPosition <= m:
                priorPosition = 0
                while priorPosition <= m:
                    if currentPosition > priorPosition:
                        val = acc[rowNum - 1][currentPosition] - acc[rowNum - 1][priorPosition]
                        if holdAccepted[currentPosition] < storedRejected[priorPosition] + val:
                            holdAccepted[currentPosition] = storedRejected[priorPosition] + val
                        if holdRejected[currentPosition] < storedRejected[priorPosition] + val:
                            holdRejected[currentPosition] = storedRejected[priorPosition] + val
                    else:
                        val = acc[rowNum][priorPosition] - acc[rowNum][currentPosition]
                        if holdAccepted[currentPosition] < storedAccepted[priorPosition] + val:
                            holdAccepted[currentPosition] = storedAccepted[priorPosition] + val
                        if holdRejected[currentPosition] < storedAccepted[priorPosition]:
                            holdRejected[currentPosition] = storedAccepted[priorPosition]
                    priorPosition += 1
                currentPosition += 1

            storedAccepted = holdAccepted
            storedRejected = holdRejected
            rowNum += 1

        maximumValue = storedAccepted[0]
        for value in storedAccepted[1:]:
            if value > maximumValue:
                maximumValue = value

        return maximumValue