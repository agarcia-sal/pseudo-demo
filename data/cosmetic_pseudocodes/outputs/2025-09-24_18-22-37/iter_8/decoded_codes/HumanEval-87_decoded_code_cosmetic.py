from typing import List, Tuple

def get_row(matrix: List[List[int]], number: int) -> List[Tuple[int, int]]:
    coordinates_list: List[Tuple[int, int]] = []
    row_counter: int = 0
    while row_counter < len(matrix):
        current_row = matrix[row_counter]
        col_counter: int = 0
        while col_counter < len(current_row):
            cell_value = current_row[col_counter]
            if not (cell_value != number):
                coordinates_list.append((row_counter, col_counter))
            col_counter += 1
        row_counter += 1

    temp_sorted_by_col_desc = sorted(coordinates_list, key=lambda x: x[1], reverse=True)
    coordinates_list = sorted(temp_sorted_by_col_desc, key=lambda x: x[0])
    return coordinates_list