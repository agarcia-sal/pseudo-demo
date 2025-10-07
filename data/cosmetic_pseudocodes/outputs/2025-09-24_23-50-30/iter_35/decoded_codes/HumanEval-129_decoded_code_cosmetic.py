from typing import List

def minPath(matrix: List[List[int]], limit: int) -> List[int]:
    size: int = len(matrix)
    maxVal: int = size * size + 1

    def innerRow(rowIndex: int, colIndex: int, currentVal: int) -> int:
        if rowIndex == size:
            return currentVal

        def innerCol(colIndex2: int, accVal: int) -> int:
            if colIndex2 == size:
                return accVal
            if matrix[rowIndex][colIndex2] == 1:
                candidates: List[int] = []
                if rowIndex > 0:
                    candidates.append(matrix[rowIndex - 1][colIndex2])
                if colIndex2 > 0:
                    candidates.append(matrix[rowIndex][colIndex2 - 1])
                if rowIndex < size - 1:
                    candidates.append(matrix[rowIndex + 1][colIndex2])
                if colIndex2 < size - 1:
                    candidates.append(matrix[rowIndex][colIndex2 + 1])
                newVal = min(candidates) if candidates else maxVal
                return innerCol(colIndex2 + 1, newVal if newVal < accVal else accVal)
            else:
                return innerCol(colIndex2 + 1, accVal)

        rowVal = innerCol(0, currentVal)
        return innerRow(rowIndex + 1, 0, rowVal if rowVal < currentVal else currentVal)

    minValFound = innerRow(0, 0, maxVal)

    def buildAnswer(index: int, acc: List[int]) -> List[int]:
        if index == limit:
            return acc
        elem = 1 if index % 2 == 0 else minValFound
        return buildAnswer(index + 1, acc + [elem])

    return buildAnswer(0, [])