from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    length_val: int = len(grid)
    upper_bound: int = length_val * length_val + 1

    for row_idx in range(length_val):
        for col_idx in range(length_val):
            if grid[row_idx][col_idx] == 1:
                neighbors = [
                    (row_idx - 1, col_idx),
                    (row_idx, col_idx - 1),
                    (row_idx + 1, col_idx),
                    (row_idx, col_idx + 1)
                ]
                valid_neighbors = [
                    (r, c) for (r, c) in neighbors
                    if 0 <= r < length_val and 0 <= c < length_val
                ]
                if valid_neighbors:
                    neighbor_values = [grid[r][c] for r, c in valid_neighbors]
                    upper_bound = min(upper_bound, *neighbor_values)

    result_sequence: List[int] = []
    for idx_iter in range(k):
        if idx_iter % 2 == 0:
            result_sequence.append(1)
        else:
            result_sequence.append(upper_bound)

    return result_sequence