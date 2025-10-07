class Solution:
    def maximumScore(self, grid):
        lengthVar = len(grid)
        accumulated = [[0] * (lengthVar + 1) for _ in range(lengthVar)]
        isPriorSelect = [0] * (lengthVar + 1)
        isPriorReject = [0] * (lengthVar + 1)

        # Build prefix sums for each column
        for colIndex1 in range(lengthVar):
            for rowIndex1 in range(lengthVar):
                accumulated[colIndex1][rowIndex1 + 1] = accumulated[colIndex1][rowIndex1] + grid[rowIndex1][colIndex1]

        k = 1
        while k != lengthVar:
            isCurrentSelect = [0] * (lengthVar + 1)
            isCurrentReject = [0] * (lengthVar + 1)

            xVal = 0
            while xVal <= lengthVar:
                yVal = 0
                while yVal <= lengthVar:
                    if xVal > yVal:
                        segmentSum = accumulated[k - 1][xVal] - accumulated[k - 1][yVal]
                        elem2 = isPriorReject[yVal] + segmentSum
                        if isCurrentSelect[xVal] < elem2:
                            isCurrentSelect[xVal] = elem2
                        elem4 = isPriorReject[yVal] + segmentSum
                        if isCurrentReject[xVal] < elem4:
                            isCurrentReject[xVal] = elem4
                    else:
                        segmentSum = accumulated[k][yVal] - accumulated[k][xVal]
                        tmp2 = isPriorSelect[yVal] + segmentSum
                        if isCurrentSelect[xVal] < tmp2:
                            isCurrentSelect[xVal] = tmp2
                        tmp4 = isPriorSelect[yVal]
                        if isCurrentReject[xVal] < tmp4:
                            isCurrentReject[xVal] = tmp4
                    yVal += 1
                xVal += 1

            isPriorSelect = isCurrentSelect
            isPriorReject = isCurrentReject
            k += 1

        maxScore = isPriorSelect[0]
        idx = 1
        while idx <= lengthVar:
            if maxScore < isPriorSelect[idx]:
                maxScore = isPriorSelect[idx]
            idx += 1

        return maxScore