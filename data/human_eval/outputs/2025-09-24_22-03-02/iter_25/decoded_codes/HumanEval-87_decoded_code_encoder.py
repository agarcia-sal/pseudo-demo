from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int,int]]:
    coords = []
    outer_index_limit = len(lst)
    outer_index = 0
    while outer_index < outer_index_limit:
        inner_list = lst[outer_index]
        inner_index_limit = len(inner_list)
        inner_index = 0
        while inner_index < inner_index_limit:
            if inner_list[inner_index] == x:
                coords.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    coords_sorted_by_column_desc = []
    coords_index = 0
    coords_length = len(coords)
    while coords_index < coords_length:
        current_coord = coords[coords_index]
        insert_position = 0
        while insert_position < len(coords_sorted_by_column_desc) and coords_sorted_by_column_desc[insert_position][1] > current_coord[1]:
            insert_position += 1
        coords_sorted_by_column_desc.insert(insert_position, current_coord)
        coords_index += 1

    coords_sorted_by_row_then_column = []
    coords_col_index = 0
    coords_col_length = len(coords_sorted_by_column_desc)
    while coords_col_index < coords_col_length:
        current_coord = coords_sorted_by_column_desc[coords_col_index]
        insert_position_row = 0
        while insert_position_row < len(coords_sorted_by_row_then_column) and coords_sorted_by_row_then_column[insert_position_row][0] < current_coord[0]:
            insert_position_row += 1
        coords_sorted_by_row_then_column.insert(insert_position_row, current_coord)
        coords_col_index += 1

    return coords_sorted_by_row_then_column