from collections import deque
from typing import List, Tuple


def get_row(matrix_grid: List[List[int]], search_key: int) -> List[Tuple[int, int]]:
    found_pairs: deque[Tuple[int, int]] = deque()
    row_counter: int = 0
    while row_counter < len(matrix_grid):
        col_counter: int = 0
        while col_counter < len(matrix_grid[row_counter]):
            # The original condition is: IF NOT (matrix_grid[row_counter][col_counter] != search_key)
            # which is logically equivalent to: matrix_grid[row_counter][col_counter] == search_key
            if matrix_grid[row_counter][col_counter] == search_key:
                found_pairs.append((row_counter, col_counter))
            col_counter += 1
        row_counter += 1

    sorted_pairs_desc_col: List[Tuple[int, int]] = []
    temp_queue = found_pairs
    while temp_queue:
        sorted_pairs_desc_col.append(temp_queue.popleft())

    def compare_by_col_desc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[1] >= b[1]

    def compare_by_row_asc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[0] <= b[0]

    descending_col_sorted: List[Tuple[int, int]] = sorted_pairs_desc_col
    swapped = True
    while swapped:
        idx = 0
        swapped = False
        while idx < len(descending_col_sorted) - 1:
            if not compare_by_col_desc(descending_col_sorted[idx], descending_col_sorted[idx + 1]):
                descending_col_sorted[idx], descending_col_sorted[idx + 1] = (
                    descending_col_sorted[idx + 1],
                    descending_col_sorted[idx],
                )
                swapped = True
            idx += 1

    final_sorted: List[Tuple[int, int]] = descending_col_sorted
    swapped = True
    while swapped:
        idx = 0
        swapped = False
        while idx < len(final_sorted) - 1:
            if not compare_by_row_asc(final_sorted[idx], final_sorted[idx + 1]):
                final_sorted[idx], final_sorted[idx + 1] = final_sorted[idx + 1], final_sorted[idx]
                swapped = True
            idx += 1

    return final_sorted