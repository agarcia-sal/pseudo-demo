from typing import List


def minPath(matrix: List[List[int]], limit: int) -> List[int]:
    size: int = len(matrix)
    threshold: int = (size * size) + 1

    def scanRow(rowIndex: int, currentThreshold: int) -> int:
        if rowIndex >= size:
            return currentThreshold

        def scanColumn(colIndex: int, currentVal: int) -> int:
            if colIndex >= size:
                return currentVal

            if matrix[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex != 0:
                    neighbors.append(matrix[rowIndex - 1][colIndex])
                if colIndex != 0:
                    neighbors.append(matrix[rowIndex][colIndex - 1])
                if rowIndex != (size - 1):
                    neighbors.append(matrix[rowIndex + 1][colIndex])
                if colIndex != (size - 1):
                    neighbors.append(matrix[rowIndex][colIndex + 1])
                if neighbors:
                    currentVal = min(neighbors)

            return scanColumn(colIndex + 1, currentVal)

        return scanRow(rowIndex + 1, scanColumn(0, currentThreshold))

    threshold = scanRow(0, threshold)

    resultSequence: List[int] = []

    def buildResult(index: int) -> None:
        if index >= limit:
            return
        resultSequence.append(1 if index % 2 == 0 else threshold)
        buildResult(index + 1)

    buildResult(0)

    return resultSequence