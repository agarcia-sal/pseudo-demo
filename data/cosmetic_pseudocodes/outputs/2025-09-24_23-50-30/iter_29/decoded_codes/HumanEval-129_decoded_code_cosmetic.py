from typing import List


def minPath(matrix: List[List[int]], p: int) -> List[int]:
    m = len(matrix)
    w = m * m + 1  # Initial large value

    for x in range(m):
        for y in range(m):
            if matrix[x][y] == 1:
                neighbors: List[int] = []
                if x > 0:
                    neighbors.append(matrix[x - 1][y])
                if y > 0:
                    neighbors.append(matrix[x][y - 1])
                if x < m - 1:
                    neighbors.append(matrix[x + 1][y])
                if y < m - 1:
                    neighbors.append(matrix[x][y + 1])
                if neighbors:
                    w = min(neighbors)

    resultArray: List[int] = []
    for index in range(p):
        resultArray.append(1 if index % 2 == 0 else w)

    return resultArray