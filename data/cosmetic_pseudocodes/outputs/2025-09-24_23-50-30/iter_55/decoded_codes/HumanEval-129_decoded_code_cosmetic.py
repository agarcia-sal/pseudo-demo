from typing import List

def minPath(matrix: List[List[int]], param: int) -> List[int]:
    lengthVar: int = len(matrix)
    minVal: int = (lengthVar * lengthVar) + 1

    def iterateColumns(row: int, col: int) -> None:
        nonlocal minVal
        if col >= lengthVar:
            return
        if matrix[row][col] == 1:
            neighbors: List[int] = []
            if row > 0:
                neighbors.append(matrix[row - 1][col])
            if col > 0:
                neighbors.append(matrix[row][col - 1])
            if row < lengthVar - 1:
                neighbors.append(matrix[row + 1][col])
            if col < lengthVar - 1:
                neighbors.append(matrix[row][col + 1])
            if neighbors:
                minVal = min(minVal, min(neighbors))
        iterateColumns(row, col + 1)

    def iterateRows(r: int) -> None:
        if r >= lengthVar:
            return
        iterateColumns(r, 0)
        iterateRows(r + 1)

    iterateRows(0)

    resultArr: List[int] = []

    def buildResult(index: int) -> None:
        if index >= param:
            return
        resultArr.append(1 if index % 2 == 0 else minVal)
        buildResult(index + 1)

    buildResult(0)
    return resultArr