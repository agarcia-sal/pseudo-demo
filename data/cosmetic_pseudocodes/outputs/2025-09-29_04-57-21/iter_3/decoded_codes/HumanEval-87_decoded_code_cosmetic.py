from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    for row_cursor in range(len(two_dimensional_list)):
        for col_cursor in range(len(two_dimensional_list[row_cursor])):
            if two_dimensional_list[row_cursor][col_cursor] == target_integer:
                hit = (row_cursor, col_cursor)
                found_positions.append(hit)
    # Sort descending by column index
    found_positions.sort(key=lambda x: x[1], reverse=True)
    # Then stable sort ascending by row index
    found_positions.sort(key=lambda x: x[0])
    return found_positions