from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    row_counter = 0
    while row_counter < len(two_dimensional_list):
        col_counter = 0
        while col_counter < len(two_dimensional_list[row_counter]):
            if two_dimensional_list[row_counter][col_counter] == target_integer:
                found_positions.append((row_counter, col_counter))
            col_counter += 1
        row_counter += 1
    # Sort by column descending, stable
    found_positions.sort(key=lambda pos: -pos[1])
    # Then sort by row ascending, stable
    found_positions.sort(key=lambda pos: pos[0])
    return found_positions