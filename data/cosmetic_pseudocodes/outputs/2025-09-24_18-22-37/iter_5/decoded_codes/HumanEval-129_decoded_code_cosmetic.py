from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    minimum_value: int = size * size + 1

    for row_index in range(size):
        for column_index in range(size):
            if grid[row_index][column_index] == 1:
                neighbors: List[int] = []
                if row_index != 0:
                    neighbors.append(grid[row_index - 1][column_index])
                if column_index != 0:
                    neighbors.append(grid[row_index][column_index - 1])
                if row_index != size - 1:
                    neighbors.append(grid[row_index + 1][column_index])
                if column_index != size - 1:
                    neighbors.append(grid[row_index][column_index + 1])

                if neighbors:
                    temp_min = neighbors[0]
                    for idx in range(1, len(neighbors)):
                        if neighbors[idx] < temp_min:
                            temp_min = neighbors[idx]
                    minimum_value = temp_min

    result: List[int] = []
    for count in range(k):
        if count % 2 == 0:
            result.append(1)
        else:
            result.append(minimum_value)

    return result