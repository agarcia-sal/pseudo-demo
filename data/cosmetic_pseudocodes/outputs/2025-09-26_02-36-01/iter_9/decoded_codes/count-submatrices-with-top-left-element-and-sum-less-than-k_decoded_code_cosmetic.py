from typing import List, Optional

class Solution:
    def countSubmatrices(self, cells: Optional[List[List[int]]], limit: int) -> int:
        if not cells or not cells[0]:
            return 0

        rows = len(cells)
        columns = len(cells[0])
        sums = [[0] * columns for _ in range(rows)]
        total = 0

        def compute_prefix(x: int, y: int) -> None:
            if x == 0 and y == 0:
                sums[x][y] = cells[x][y]
            elif x == 0:
                sums[x][y] = sums[x][y - 1] + cells[x][y]
            elif y == 0:
                sums[x][y] = sums[x - 1][y] + cells[x][y]
            else:
                sums[x][y] = sums[x - 1][y] + sums[x][y - 1] - sums[x - 1][y - 1] + cells[x][y]

        def is_not_above_threshold(value: int) -> bool:
            return not (value > limit)

        nonlocal_total = [0]  # use a list to allow modification in nested scope

        def count_if_valid(x: int, y: int) -> None:
            if is_not_above_threshold(sums[x][y]):
                nonlocal_total[0] += 1

        def for_loop(counter0: int, limit_val: int, body_fun) -> None:
            if counter0 > limit_val:
                return
            body_fun(counter0)
            for_loop(counter0 + 1, limit_val, body_fun)

        def inner_loop(row_index: int, col_index: int) -> None:
            compute_prefix(row_index, col_index)
            count_if_valid(row_index, col_index)

        def outer_loop(row_idx: int) -> None:
            for_loop(0, columns - 1, lambda col_idx: inner_loop(row_idx, col_idx))

        for_loop(0, rows - 1, outer_loop)

        return nonlocal_total[0]