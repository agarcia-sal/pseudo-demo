class Solution:
    def maximumScore(self, grid):
        lengthGrid = 0
        while lengthGrid < len(grid):
            lengthGrid += 1

        def initializeMatrix(rows, cols, val):
            res = []
            idxRow = 0
            while idxRow < rows:
                tempRow = []
                idxCol = 0
                while idxCol < cols:
                    tempRow.append(val)
                    idxCol += 1
                res.append(tempRow)
                idxRow += 1
            return res

        prefSum = initializeMatrix(lengthGrid, lengthGrid + 1, 0)

        prevChosen = []
        prevIgnored = []
        idxFill = 0
        while idxFill <= lengthGrid:
            prevChosen.append(0)
            prevIgnored.append(0)
            idxFill += 1

        colIdx = 0
        while colIdx < lengthGrid:
            rowIdx = 0
            while rowIdx < lengthGrid:
                prefSum[colIdx][rowIdx + 1] = prefSum[colIdx][rowIdx] + grid[rowIdx][colIdx]
                rowIdx += 1
            colIdx += 1

        rowCount = 1
        while True:
            if rowCount == lengthGrid:
                break

            currChosen = []
            currIgnored = []
            fillIdx = 0
            while fillIdx < lengthGrid + 1:
                currChosen.append(0)
                currIgnored.append(0)
                fillIdx += 1

            indexCurr = 0
            while indexCurr < lengthGrid + 1:

                indexPrev = 0
                while indexPrev < lengthGrid + 1:

                    if indexCurr > indexPrev:
                        segScore = prefSum[rowCount - 1][indexCurr] - prefSum[rowCount - 1][indexPrev]
                        if currChosen[indexCurr] < prevIgnored[indexPrev] + segScore:
                            currChosen[indexCurr] = prevIgnored[indexPrev] + segScore
                        if currIgnored[indexCurr] < prevIgnored[indexPrev] + segScore:
                            currIgnored[indexCurr] = prevIgnored[indexPrev] + segScore
                    else:
                        segScore = prefSum[rowCount][indexPrev] - prefSum[rowCount][indexCurr]
                        if currChosen[indexCurr] < prevChosen[indexPrev] + segScore:
                            currChosen[indexCurr] = prevChosen[indexPrev] + segScore
                        if currIgnored[indexCurr] < prevChosen[indexPrev]:
                            currIgnored[indexCurr] = prevChosen[indexPrev]

                    indexPrev += 1

                indexCurr += 1

            prevChosen = currChosen
            prevIgnored = currIgnored

            rowCount += 1

        def findMaximum(arr):
            maxVal = arr[0]
            idxMax = 1
            while idxMax < len(arr):
                if arr[idxMax] > maxVal:
                    maxVal = arr[idxMax]
                idxMax += 1
            return maxVal

        return findMaximum(prevChosen)