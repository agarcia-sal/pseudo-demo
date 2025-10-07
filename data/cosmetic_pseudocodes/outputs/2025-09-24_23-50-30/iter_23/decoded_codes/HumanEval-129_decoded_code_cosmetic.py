from typing import List


def minPath(matrix: List[List[int]], limit: int) -> List[int]:
    size: int = len(matrix)
    threshold: int = (size * size) + 1
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == 1:
                neighborhood: set[int] = set()
                if row != 0:
                    neighborhood.add(matrix[row - 1][column])
                if column != 0:
                    neighborhood.add(matrix[row][column - 1])
                if row != size - 1:
                    neighborhood.add(matrix[row + 1][column])
                if column != size - 1:
                    neighborhood.add(matrix[row][column + 1])
                if neighborhood:
                    threshold = min(threshold, min(neighborhood))
    output: List[int] = [(1 if index % 2 == 0 else threshold) for index in range(limit)]
    return output