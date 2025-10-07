from typing import List

def minPath(matrix: List[List[int]], limit: int) -> List[int]:
    n: int = len(matrix)
    threshold: int = (n * n) + 1

    row_index: int = 0
    while row_index < n:
        col_index: int = 0
        while col_index < n:
            cell: int = matrix[row_index][col_index]
            if cell == 1:
                neighbors: List[int] = []
                if row_index != 0:
                    neighbors.append(matrix[row_index - 1][col_index])
                if col_index != 0:
                    neighbors.append(matrix[row_index][col_index - 1])
                if row_index != n - 1:
                    neighbors.append(matrix[row_index + 1][col_index])
                if col_index != n - 1:
                    neighbors.append(matrix[row_index][col_index + 1])
                if neighbors:
                    threshold = min(neighbors)
            col_index += 1
        row_index += 1

    output: List[int] = []
    for counter in range(limit):
        if counter % 2 == 0:
            output.append(1)
        else:
            output.append(threshold)

    return output