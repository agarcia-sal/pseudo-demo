from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    dim: int = len(grid)
    bound: int = (dim * dim) + 1  # initial large bound

    def computeMinForCell(x_idx: int, y_idx: int) -> int:
        if grid[x_idx][y_idx] == 1:
            neighbors: List[int] = []
            if x_idx != 0:
                neighbors.append(grid[x_idx - 1][y_idx])
            if y_idx != 0:
                neighbors.append(grid[x_idx][y_idx - 1])
            if x_idx != dim - 1:
                neighbors.append(grid[x_idx + 1][y_idx])
            if y_idx != dim - 1:
                neighbors.append(grid[x_idx][y_idx + 1])
            return min(neighbors) if neighbors else bound
        else:
            return bound

    row_index: int = 0
    while row_index < dim:
        col_index: int = 0
        while col_index < dim:
            computed_min = computeMinForCell(row_index, col_index)
            if computed_min < bound:
                bound = computed_min
            col_index += 1
        row_index += 1

    resultAccumulator: List[int] = []

    def fillResults(counter: int) -> None:
        if counter >= k:
            return
        if counter % 2 == 0:
            resultAccumulator.append(1)
        else:
            resultAccumulator.append(bound)
        fillResults(counter + 1)

    fillResults(0)

    return resultAccumulator