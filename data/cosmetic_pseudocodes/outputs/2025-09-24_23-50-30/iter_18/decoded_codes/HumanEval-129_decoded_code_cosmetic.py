from typing import List, Dict, Optional


def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    u: int = n * n + 1

    def iterate_col_idx(row_idx: int, col_idx: int) -> None:
        nonlocal u
        if col_idx == n:
            return
        if grid[row_idx][col_idx] == 1:
            adj_values: Dict[str, int] = {}
            if row_idx != 0:
                adj_values["up"] = grid[row_idx - 1][col_idx]
            if col_idx != 0:
                adj_values["left"] = grid[row_idx][col_idx - 1]
            if row_idx != n - 1:
                adj_values["down"] = grid[row_idx + 1][col_idx]
            if col_idx != n - 1:
                adj_values["right"] = grid[row_idx][col_idx + 1]
            min_adj: Optional[int] = None
            for val in adj_values.values():
                if min_adj is None or val < min_adj:
                    min_adj = val
            if min_adj is not None:
                u = min_adj
        iterate_col_idx(row_idx, col_idx + 1)

    def iterate_row_idx(row_idx: int) -> None:
        if row_idx == n:
            return
        iterate_col_idx(row_idx, 0)
        iterate_row_idx(row_idx + 1)

    iterate_row_idx(0)

    result: List[int] = []
    index: int = 0
    while index < k:
        if (index // 2) * 2 == index:
            value_to_append = 1
        else:
            value_to_append = u
        result.append(value_to_append)
        index += 1

    return result