from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = (size * size) + 1
    result_val: int = limit

    def traverse(cellIndex: int) -> None:
        nonlocal result_val
        if cellIndex < 0 or cellIndex >= size * size:
            return

        row, col = divmod(cellIndex, size)

        if grid[row][col] == 1:
            neighbors = set()
            if row > 0:
                neighbors.add(grid[row - 1][col])
            if col > 0:
                neighbors.add(grid[row][col - 1])
            if row < size - 1:
                neighbors.add(grid[row + 1][col])
            if col < size - 1:
                neighbors.add(grid[row][col + 1])
            if neighbors:
                min_neighbor = min(neighbors)
                result_val = min_neighbor  # update nonlocal result_val

        traverse(cellIndex + 1)

    traverse(0)

    output: List[int] = []
    index: int = 0
    while index < k:
        if index % 2 == 0:
            output.append(1)
        else:
            output.append(result_val)
        index += 1

    return output