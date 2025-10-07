from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    row_counter: int = 0
    while row_counter < len(two_dimensional_list):
        column_counter: int = 0
        while column_counter < len(two_dimensional_list[row_counter]):
            if not (two_dimensional_list[row_counter][column_counter] != target_integer):
                position_pair = (row_counter, column_counter)
                found_positions.append(position_pair)
            column_counter += 1
        row_counter += 1

    # sort by column descending first, then by row ascending
    found_positions.sort(key=lambda element: -element[1])
    found_positions.sort(key=lambda element: element[0])
    return found_positions