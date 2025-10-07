from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rowCount = len(image)
        colCount = len(image[0]) if rowCount > 0 else 0

        # Initialize outputGrid and tallyGrid with zeros
        outputGrid = [[0] * colCount for _ in range(rowCount)]
        tallyGrid = [[0] * colCount for _ in range(rowCount)]

        def is_valid_region(x: int, y: int) -> bool:
            deltaPairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for iVal in range(x, x + 3):
                for jVal in range(y, y + 3):
                    for dx, dy in deltaPairs:
                        neighborX = iVal + dx
                        neighborY = jVal + dy
                        if 0 <= neighborX < x + 3 and 0 <= neighborY < y + 3:
                            diffVal = image[iVal][jVal] - image[neighborX][neighborY]
                            if diffVal < 0:
                                diffVal = -diffVal
                            if diffVal > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            sumVal = 0
            for rowIdx in range(x, x + 3):
                for colIdx in range(y, y + 3):
                    sumVal += image[rowIdx][colIdx]
            averageVal = sumVal // 9
            return averageVal

        iIter = 0
        while iIter <= rowCount - 3:
            jIter = 0
            while jIter <= colCount - 3:
                if is_valid_region(iIter, jIter):
                    avgVal = calculate_average(iIter, jIter)
                    xIter = iIter
                    while xIter != iIter + 3:
                        yIter = jIter
                        while yIter != jIter + 3:
                            outputGrid[xIter][yIter] += avgVal
                            tallyGrid[xIter][yIter] += 1
                            yIter += 1
                        xIter += 1
                jIter += 1
            iIter += 1

        idxRow = 0
        while idxRow != rowCount:
            idxCol = 0
            while idxCol != colCount:
                if tallyGrid[idxRow][idxCol] > 0:
                    outputGrid[idxRow][idxCol] //= tallyGrid[idxRow][idxCol]
                else:
                    outputGrid[idxRow][idxCol] = image[idxRow][idxCol]
                idxCol += 1
            idxRow += 1

        return outputGrid