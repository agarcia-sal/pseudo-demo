from typing import List, Tuple

def get_row(lst: List[List], x) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    outer_index = 0
    while outer_index < len(lst):
        inner_list = lst[outer_index]
        inner_index = 0
        while inner_index < len(inner_list):
            element = inner_list[inner_index]
            if element == x:
                coords.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1
    coords_sorted_columns_descending: List[Tuple[int, int]] = []
    index_column = 0
    while index_column < len(coords):
        current_coordinate = coords[index_column]
        insert_position = 0
        while (insert_position < len(coords_sorted_columns_descending) and
               coords_sorted_columns_descending[insert_position][1] > current_coordinate[1]):
            insert_position += 1
        coords_sorted_columns_descending.insert(insert_position, current_coordinate)
        index_column += 1
    coords_sorted_rows_ascending: List[Tuple[int, int]] = []
    index_row = 0
    while index_row < len(coords_sorted_columns_descending):
        current_coordinate = coords_sorted_columns_descending[index_row]
        insert_position = 0
        while (insert_position < len(coords_sorted_rows_ascending) and
               coords_sorted_rows_ascending[insert_position][0] <= current_coordinate[0]):
            insert_position += 1
        coords_sorted_rows_ascending.insert(insert_position, current_coordinate)
        index_row += 1
    return coords_sorted_rows_ascending