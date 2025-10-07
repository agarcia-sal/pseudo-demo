from typing import List


def minPath(matrix: List[List[int]], amount: int) -> List[int]:
    length: int = len(matrix)
    value: int = (length * length) + 1
    rowIndex: int = 0
    while rowIndex < length:
        colIndex: int = 0
        while colIndex < length:
            # Check if matrix[rowIndex][colIndex] == 1
            if matrix[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                condA = rowIndex != 0
                condB = colIndex != 0
                condC = rowIndex != (length - 1)
                condD = colIndex != (length - 1)
                if condA:
                    neighbors.append(matrix[rowIndex - 1][colIndex])
                if condB:
                    neighbors.append(matrix[rowIndex][colIndex - 1])
                if condC:
                    neighbors.append(matrix[rowIndex + 1][colIndex])
                if condD:
                    neighbors.append(matrix[rowIndex][colIndex + 1])
                min_neighbor = min(neighbors) if neighbors else value
                # Update value to min(value, min_neighbor)
                value = value if value < min_neighbor else min_neighbor
            colIndex += 1
        rowIndex += 1

    result: List[int] = []
    index: int = 0
    while index < amount:
        isEven = (index % 2) == 0
        toAppend = (1 if isEven else value)
        result.append(toAppend)
        index += 1
    return result