from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    accumulator: List[Tuple[int, int]] = []
    row_counter: int = 0
    while row_counter < len(two_dimensional_list):
        col_counter: int = 0
        while col_counter < len(two_dimensional_list[row_counter]):
            if two_dimensional_list[row_counter][col_counter] == target_integer:
                accumulator.append((row_counter, col_counter))
            col_counter += 1
        row_counter += 1
    # Sort first by descending column index, then by ascending row index
    sorted_by_column_desc = sorted(accumulator, key=lambda x: -x[1])
    final_sorted = sorted(sorted_by_column_desc, key=lambda x: x[0])
    return final_sorted