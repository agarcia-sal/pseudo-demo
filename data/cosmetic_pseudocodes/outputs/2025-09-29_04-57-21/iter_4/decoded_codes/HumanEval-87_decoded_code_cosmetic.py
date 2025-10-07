from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    row_cursor: int = 0
    while row_cursor < len(two_dimensional_list):
        col_cursor: int = 0
        while col_cursor < len(two_dimensional_list[row_cursor]):
            if not (two_dimensional_list[row_cursor][col_cursor] != target_integer):
                found_positions.append((row_cursor, col_cursor))
            col_cursor += 1
        row_cursor += 1
    temp_first_sort = sorted(found_positions, key=lambda x: x[0])
    final_sort = sorted(temp_first_sort, key=lambda x: x[1], reverse=True)
    return final_sort