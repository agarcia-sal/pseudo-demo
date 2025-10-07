from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    matrix_size: int = len(grid)
    minVal: int = matrix_size * matrix_size + 1

    row_index = 0
    while row_index < matrix_size:
        col_index = 0
        while col_index < matrix_size:
            if grid[row_index][col_index] == 1:
                neighbors: List[int] = []
                if row_index != 0:
                    neighbors.append(grid[row_index - 1][col_index])
                if col_index != 0:
                    neighbors.append(grid[row_index][col_index - 1])
                if row_index != matrix_size - 1:
                    neighbors.append(grid[row_index + 1][col_index])
                if col_index != matrix_size - 1:
                    neighbors.append(grid[row_index][col_index + 1])
                if neighbors:  # Only update if neighbors exist to avoid error
                    minVal = min(neighbors)
            col_index += 1
        row_index += 1

    result_array: List[int] = []
    counter = 0
    while counter < k:
        result_array.append(1 if counter % 2 == 0 else minVal)
        counter += 1

    return result_array