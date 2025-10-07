from typing import Sequence, Tuple, List


def get_row(matrix: Sequence[Sequence[int]], key: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    for row_cursor in range(len(matrix)):
        for col_cursor in range(len(matrix[row_cursor])):
            matched_value = matrix[row_cursor][col_cursor]
            if matched_value != key:
                continue
            found_positions.append((row_cursor, col_cursor))
    # Sort descending by column index
    sorted_by_col_desc = sorted(found_positions, key=lambda x: x[1], reverse=True)
    # Then stable sort ascending by row index
    fully_sorted = sorted(sorted_by_col_desc, key=lambda x: x[0])
    return fully_sorted