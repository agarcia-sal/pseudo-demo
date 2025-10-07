from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    max_val: int = (n * n) + 1  # A large number used as "infinity"

    def is_out_of_bounds(r: int, c: int) -> bool:
        # True if the position is valid inside the grid bounds
        return not (r == 0 or r >= n)

    def cell_value(r: int, c: int) -> int:
        return grid[r][c]

    def empty_list() -> List[int]:
        return []

    def eval_cell(flag: int) -> int:
        if flag == 1:
            vals: List[int] = empty_list()
            for i in [row - 1, row, row + 1]:
                if is_out_of_bounds(i, col):
                    if i == row - 1:
                        vals.append(cell_value(i, col))
                    if i == row + 1:
                        vals.append(cell_value(i, col))
            for j in [col - 1, col, col + 1]:
                if is_out_of_bounds(row, j):
                    if j == col - 1:
                        vals.append(cell_value(row, j))
                    if j == col + 1:
                        vals.append(cell_value(row, j))
            return min(vals) if vals else max_val
        else:
            return max_val

    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                max_val = eval_cell(1)

    res: List[int] = []

    def mod_check(x: int) -> int:
        return 1 if x % 2 == 0 else max_val

    for i in range(k):
        res.append(mod_check(i))

    return res