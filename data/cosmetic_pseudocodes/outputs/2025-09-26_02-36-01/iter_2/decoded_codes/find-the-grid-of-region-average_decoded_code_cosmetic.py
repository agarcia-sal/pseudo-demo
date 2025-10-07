from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rowCount = len(image)
        colCount = len(image[0])
        outputMatrix = [[0 for _ in range(colCount)] for _ in range(rowCount)]
        frequencyMatrix = [[0 for _ in range(colCount)] for _ in range(rowCount)]

        def is_valid_region(x: int, y: int) -> bool:
            dxdyPairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            rowEnd = x + 3
            colEnd = y + 3
            rowIdx = x
            while rowIdx < rowEnd:
                colIdx = y
                while colIdx < colEnd:
                    for dx, dy in dxdyPairs:
                        neighborX = rowIdx + dx
                        neighborY = colIdx + dy
                        if 0 <= neighborX < rowEnd and 0 <= neighborY < colEnd:
                            diffValue = image[rowIdx][colIdx] - image[neighborX][neighborY]
                            if abs(diffValue) > threshold:
                                return False
                    colIdx += 1
                rowIdx += 1
            return True

        def calculate_average(x: int, y: int) -> int:
            sumValue = 0
            endX = x + 3
            endY = y + 3
            for rowIter in range(x, endX):
                for colIter in range(y, endY):
                    sumValue += image[rowIter][colIter]
            averagePixel = sumValue // 9
            return averagePixel

        mainRowIdx = 0
        while mainRowIdx < rowCount - 2:
            mainColIdx = 0
            while mainColIdx < colCount - 2:
                if is_valid_region(mainRowIdx, mainColIdx):
                    regionAvg = calculate_average(mainRowIdx, mainColIdx)
                    fillRow = mainRowIdx
                    while fillRow < mainRowIdx + 3:
                        fillCol = mainColIdx
                        while fillCol < mainColIdx + 3:
                            outputMatrix[fillRow][fillCol] += regionAvg
                            frequencyMatrix[fillRow][fillCol] += 1
                            fillCol += 1
                        fillRow += 1
                mainColIdx += 1
            mainRowIdx += 1

        for rIndex in range(rowCount):
            for cIndex in range(colCount):
                freqVal = frequencyMatrix[rIndex][cIndex]
                if freqVal > 0:
                    sumVal = outputMatrix[rIndex][cIndex]
                    normalizedVal = sumVal // freqVal
                    outputMatrix[rIndex][cIndex] = normalizedVal
                else:
                    outputMatrix[rIndex][cIndex] = image[rIndex][cIndex]

        return outputMatrix